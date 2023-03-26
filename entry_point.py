import Tests.app_test as at
import Tests.post_train_data_test as ptdt
import Tests.post_presentation_data_test as ppdt


if __name__ == "__main__":
    # run new example throw model test 
    at.run_app_test()

    # run all post_train_data Db table tests
    #ptdt.run_post_train_data_tests()
    
    # run all post_presentation_data Db table tests
    #ppdt.run_post_presentation_data_tests()