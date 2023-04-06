from DAL.post_train_data_dal import PostTrainDataDAL, PostTrainDataStatusID
from DAL.post_train_data_dal import PredValsIndex, PostTrainDataStatusID
from DAL.post_data_base_dal import PostDataBase
from DAL.db_clients import SocialMediaDbClient
from configparser import ConfigParser
from Utils.numbers import Numbers
from typing import Iterable
import asyncio
import openai


class GptWriterEngine():
    
    def __init__(self, config: ConfigParser, db_client: SocialMediaDbClient) -> None:
        self.__db_client = db_client
        self.__api_key = config.get('GPT', 'ApiKey')

    async def write_labels_to_db(self) -> Iterable[PostDataBase]:
        try:
            async_session = self.__db_client.get_async_session()
            async with async_session() as session:
                async with session.begin():
                    ptd_dal = PostTrainDataDAL(session)
                    all_new_posts = await ptd_dal.get_post_train_data_by_status(
                            PostTrainDataStatusID.NEW.value)
            print(f'\nFetched {len(all_new_posts)} db tweets with status new\n')

            labels_dict = {}
            for new_post in all_new_posts:
                labels_str = await self.get_labels(new_post.content)
                labels_entry = self.get_labels_dict(labels_str)       
                labels_dict.update({new_post.id: labels_entry})
                await asyncio.sleep(5)
            print(f'\Got {len(labels_dict)} labels from GPT\n')

            for id, labels_list, i in zip(labels_dict.keys(), labels_dict.values(), range(0,len(labels_dict))):
                print(f'\Start processing tweet {i}/{len(labels_dict)}\n')
                async_session = self.__db_client.get_async_session()
                async with async_session() as session:
                    async with session.begin():
                        ptd_dal = PostTrainDataDAL(session)
                        all_new_posts = await ptd_dal.update_post_train_data_by_id(
                            id=id, 
                            toxic=labels_list[PredValsIndex.TOXIC.name],
                            severe_toxic=labels_list[PredValsIndex.SEVERE_TOXIC.name],
                            obscene=labels_list[PredValsIndex.OBSCENE.name],
                            threat=labels_list[PredValsIndex.THREAT.name],
                            insult=labels_list[PredValsIndex.INSULT.name],
                            identity_hate=labels_list[PredValsIndex.IDENTITY_HATE.name],
                            status_id=PostTrainDataStatusID.PROCESSED.value)
        except Exception as e:
            print(e)
 
    async def get_labels(self, text: str, length: int=1024) -> str:
        
        openai.api_key = self.__api_key
        prompt = f"I have a sentence that I would like to categorize for those 6 " +\
                 f"categories: TOXIC, SEVERE_TOXIC, OBSCENE, THREAT, INSULT and " +\
                 f"IDENTITY_HATE. Each category can be 0 if you don't think that the " +\
                 f"sentence belong to this category or 1 if you do think it belongs to it." +\
                 f"Here is the sentence: \"{text}\". " +\
                 f"Could you tell me what would be your number for each category?"
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0301",
              messages = [
                {'role': 'user', 'content': prompt}
            ],
            temperature = 0 )
        return response['choices'][0]['message']['content']
    
    def get_labels_dict(self, labels_str: str) -> dict:
        
        if Numbers.has_numbers(labels_str):
            labels_str_list = labels_str.split('\n')
            key_val_func = lambda l, i: l.split(':')[i].strip()
            labels_entry = {key_val_func(l, 0) : key_val_func(l, -1) for l in labels_str_list}
        else:
            labels_entry = {e.name: 0 for e in PredValsIndex}
        
        return labels_entry           