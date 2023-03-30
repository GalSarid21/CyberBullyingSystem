from DbWriter.tweets_writer import TweetWriterEngine
from DAL.db_clients import SocialMediaDbClient
from DAL.social_media_dto import PostDataType
from configparser import ConfigParser

async def tweet_writer_engine_test():
    config = ConfigParser()
    config.read("Data\\local.ini")
    db_client = SocialMediaDbClient(config)
    engine = TweetWriterEngine(config, db_client)
    failures = await engine.write_tweets_to_db(PostDataType.POST_PRESENTATION_DATA)
