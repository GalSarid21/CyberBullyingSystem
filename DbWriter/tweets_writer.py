from configparser import ConfigParser
from DbWriter.tweepy_setup import TweepyWrapper
from DAL.db_clients import SocialMediaDbClient
from DAL.post_train_data_dal import PostTrainDataDAL
from typing import Iterable


class TweetWriterEngine():

    def __init__(self, config: ConfigParser, db_client: SocialMediaDbClient) -> None:
        self.__tweepy = TweepyWrapper(config)
        self.__db_client = db_client

    async def write_tweets_to_post_train_data(self) -> Iterable[PostTrainDataDAL]:
        tweets = self.__tweepy.stream_tweets()
        async_session = self.__db_client.get_async_session()
        failures = []

        for tweet in tweets:
            try:
                async with async_session() as session:
                    async with session.begin():
                        ptd_dal = PostTrainDataDAL(session)
                        await ptd_dal.create_post_train_data('twitter', tweet.content)
            except Exception as e:
                failures.append(tweet)
        
        return failures

    async def write_tweets_to_post_presentation_data(self):
        tweets = self.__tweepy.stream_tweets()
        session = self.__db_client.get_async_session()