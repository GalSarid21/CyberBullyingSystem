import Tests.app_test as at
import Tests.post_train_data_test as ptdt
import Tests.post_presentation_data_test as ppdt
import Tests.hate_monitor_test as hmt
import Tests.tweepy_test as tt
import Tests.tweet_writer_test as twt
import Tests.gpt_writer_test as gwt
import ModelAPI.bullying_detector as bd
import asyncio

from DbWriter.db_writer_manager import DbWriterManager
from DAL.social_media_dto import PostDataType


if __name__ == "__main__":
    #region Tests
    # run new example throw model test 
    #at.run_app_test()

    # run all post_train_data Db table tests
    #asyncio.run(ptdt.run_post_train_data_tests())
    
    # run all post_presentation_data Db table tests
    #asyncio.run(ppdt.run_post_presentation_data_tests())

    # run all hate_monitor Db table tests
    #asyncio.run(hmt.run_hate_monitor_tests())

    # run tweepy stream test
    #tt.run_tweepy_stream_test()

    # run tweet writer test
    #asyncio.run(twt.tweet_writer_engine_test())

    # run flask server test
    bd.run_server_test()

    # run gpt writer test
    #asyncio.run(gwt.run_gpt_writer_test())
    # endregion

    #region Runners
    #db_writer_manager = DbWriterManager()
    #asyncio.run(db_writer_manager.write_new_tweets(PostDataType.POST_PRESENTATION_DATA))
    #endregion