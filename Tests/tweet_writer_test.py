from varname import nameof
from DbWriter.tweets_writer import TweetWriterEngine
from DAL.db_clients import SocialMediaDbClient
from DAL.social_media_dto import PostDataType
from configparser import ConfigParser

async def tweet_writer_engine_test():
    config = ConfigParser()
    config.read("Data\\local.ini")
    db_client = SocialMediaDbClient(config)
    search_terms_list = config.get('Twitter', 'SearchTermsHate')
    search_terms_list = search_terms_list.split(',')
    search_terms_list = [','.join(str(st) for st in search_terms_list[i * 3 : i * 3 + 3]) 
                                            for i in range(len(search_terms_list) // 3)]
    for search_terms_str in search_terms_list:
        print(f'\nStarting {nameof(TweetWriterEngine)}, search terms: {search_terms_str}\n')
        tweet_writer = TweetWriterEngine(config, db_client, search_terms_str)
        failures = await tweet_writer.write_tweets_to_db(PostDataType.POST_TRAIN_DATA)
