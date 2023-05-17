from configparser import ConfigParser
from DbWriter.tweepy_setup import TweepyWrapper
from DAL.twitter_dto import TweetDto
from DAL.social_media_dto import PostDataType
from DAL.db_clients import SocialMediaDbClient
from DAL.post_train_data_dal import PostTrainDataDAL
from DAL.post_presentation_data_dal import PostPresentationDataDAL
from DAL.post_data_base_dal import PostDataBase
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Iterable


class TweetWriterEngine():

    def __init__(self, config: ConfigParser, 
                 db_client: SocialMediaDbClient, 
                 search_terms_str: str) -> None:
        self.__tweepy = TweepyWrapper(config, search_terms_str)
        self.__db_client = db_client

    async def write_tweets_to_db(self, table: PostDataType) -> Iterable[PostDataBase]:
        tweets = self.__tweepy.stream_tweets()
        print(f'\nFetched {len(tweets)} from twitter\n')
        async_session = self.__db_client.get_async_session()
        failures = []

        for tweet, i in zip(tweets, range(0, len(tweets))):
            try:
                print(f'Start process tweet {i+1}/{len(tweets)}')
                async with async_session() as session:
                    async with session.begin():
                        await self.__create_new_row_by_table_type(table, tweet, session)
            except Exception as e:
                failures.append(tweet)
        
        return failures
    
    async def __create_new_row_by_table_type(self, 
                                             table: PostDataType, 
                                             tweet: TweetDto, 
                                             session: AsyncSession) -> None:
        match table:
            
            case PostDataType.POST_TRAIN_DATA:
                ptd_dal = PostTrainDataDAL(session)
                await ptd_dal.create_post_train_data('twitter', tweet.content)
            
            case PostDataType.POST_PRESENTATION_DATA:
                ppd_dal = PostPresentationDataDAL(session)
                await ppd_dal.create_post_presentation_data(
                    'twitter', tweet.content, tweet.user_name)