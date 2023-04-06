from varname import nameof
from configparser import ConfigParser
from DAL.social_media_dto import PostDataType
from DAL.db_clients import SocialMediaDbClient
from DbWriter.gpt_writer import GptWriterEngine
from DbWriter.tweets_writer import TweetWriterEngine

class DbWriterManager():

    def __init__(self) -> None:
        config = ConfigParser()
        config.read("Data\\local.ini")
        self.__config = config
        self.__db_client = SocialMediaDbClient(config)

    async def write_new_tweets(self, post_data_type: PostDataType):
        search_terms_list = self.__config.get('Twitter', 'SearchTermsHate')
        search_terms_list = search_terms_list.split(',')
        search_terms_list = [','.join(str(st) for st in search_terms_list[i * 3 : i * 3 + 3]) 
                                              for i in range(len(search_terms_list) // 3)]
        for search_terms_str in search_terms_list:
            print(f'\nStarting {nameof(TweetWriterEngine)}, search terms: {search_terms_str}\n')
            tweet_writer = TweetWriterEngine(self.__config, self.__db_client, search_terms_str)
            failures = await tweet_writer.write_tweets_to_db(post_data_type)
            
            if post_data_type == PostDataType.POST_TRAIN_DATA:
                print(f'\nStarting {nameof(GptWriterEngine)}\n')
                gpt_writer = GptWriterEngine(self.__config, self.__db_client)
                await gpt_writer.write_labels_to_db()