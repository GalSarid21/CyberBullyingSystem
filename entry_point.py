import Tests.app_test as at
import Tests.post_train_data_test as ptdt
import Tests.post_presentation_data_test as ppdt
import Tests.tweepy_test as tt
import Tests.tweet_writer_test as twt
import ModelAPI.bullying_detector as bd
import asyncio


if __name__ == "__main__":
    # run new example throw model test 
    #at.run_app_test()

    # run all post_train_data Db table tests
    #asyncio.run(ptdt.run_post_train_data_tests())
    
    # run all post_presentation_data Db table tests
    #asyncio.run(ppdt.run_post_presentation_data_tests())

    # run tweepy stream test
    #tt.run_tweepy_stream_test()

    # run tweet writer test
    #asyncio.run(twt.tweet_writer_engine_test())

    # run flask server test
    bd.run_server_test()