import asyncio
import Tests.app_test as at
from DbWriter.post_train_data_dal import PostTrainDataDAL
from DbWriter.db_clients import SocialMediaDbClient

    
async def get_all_post_train_data_test(async_session):
    async with async_session() as session:
        async with session.begin():
            ptd_dal = PostTrainDataDAL(session)
            return await ptd_dal.get_all_post_train_data()
        

if __name__ == "__main__":
    # run new example throw model test 
    #at.run_app_test()

    # db test
    db_client = SocialMediaDbClient()
    session = db_client.get_async_session()
    res = asyncio.run(get_all_post_train_data_test(session))
    print(res)