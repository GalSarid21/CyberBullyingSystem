from DbWriter.tweets_writer import TweetWriterEngine
from DAL.db_clients import SocialMediaDbClient
from configparser import ConfigParser

async def tweet_writer_engine_test():
    config = ConfigParser()
    config.read("Data\\local.ini")
    db_client = SocialMediaDbClient(config)
    engine = TweetWriterEngine(config, db_client)
    failures = await engine.write_tweets_to_post_train_data()
    a = 1
