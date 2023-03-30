import Tests.app_test as at
from DAL.post_train_data_dal import PostTrainDataDAL, PostTrainDataStatusID
from DAL.db_clients import SocialMediaDbClient
from configparser import ConfigParser

    
async def get_all_post_train_data_test(async_session):
    async with async_session() as session:
        async with session.begin():
            ptd_dal = PostTrainDataDAL(session)
            return await ptd_dal.get_all_post_train_data()
        
async def get_post_train_data_by_source_test(async_session, source):
    async with async_session() as session:
        async with session.begin():
            ptd_dal = PostTrainDataDAL(session)
            return await ptd_dal.get_post_train_data_by_source(source)

async def delete_post_train_data_by_id_test(async_session, id):
    async with async_session() as session:
        async with session.begin():
            ptd_dal = PostTrainDataDAL(session)
            return await ptd_dal.delete_post_train_data_by_id(id)

async def get_post_train_data_by_id_test(async_session, id):
    async with async_session() as session:
        async with session.begin():
            ptd_dal = PostTrainDataDAL(session)
            return await ptd_dal.get_post_train_data_by_id(id)
        
async def get_post_train_data_by_status_test(async_session, status_id):
    async with async_session() as session:
        async with session.begin():
            ptd_dal = PostTrainDataDAL(session)
            return await ptd_dal.get_post_train_data_by_status(status_id)

async def create_new_post_train_data_test(async_session, 
                                          source, 
                                          content, 
                                          toxic, 
                                          severe_toxic, 
                                          obscene, 
                                          insult, 
                                          threat, 
                                          identity_hate):
    async with async_session() as session:
        async with session.begin():
            ptd_dal = PostTrainDataDAL(session)
            return await ptd_dal.create_post_train_data(
                source, content, toxic, severe_toxic, obscene, insult, threat, identity_hate)
        
async def update_post_train_data_test(async_session, 
                                      id,
                                      source = '', 
                                      content = '', 
                                      toxic = -1, 
                                      severe_toxic = -1, 
                                      obscene = -1, 
                                      insult = -1, 
                                      threat = -1, 
                                      identity_hate = -1,
                                      status_id = -1):
    async with async_session() as session:
        async with session.begin():
            ptd_dal = PostTrainDataDAL(session)
            return await ptd_dal.update_post_train_data_by_id(
                id, source, content, toxic, severe_toxic, obscene, 
                insult, threat, identity_hate, status_id)


async def run_post_train_data_tests():
    config = ConfigParser()
    config.read("Data\\local.ini")
    
    # db_client = SocialMediaDbClient(config)
    # session = db_client.get_async_session()
    # res = await get_all_post_train_data_test(session)
    # print(res)
    
    # db_client = SocialMediaDbClient(config)
    # session = db_client.get_async_session()
    # res = await get_post_train_data_by_source_test(session, 'twitter')
    # print(res)

    # db_client = SocialMediaDbClient(config)
    # session = db_client.get_async_session()
    # res = await get_post_train_data_by_id_test(session, 1)
    # print(res.id)

    # db_client = SocialMediaDbClient(config)
    # session = db_client.get_async_session()
    # res = await create_new_post_train_data_test(
    #     session, 'twitter', 
    #     'real question is do feminist liberal bigots understand that different rules fro men/weman is sexism',
    #     1, 0, 0, 0, 1, 0)
    # print(res.id)

    db_client = SocialMediaDbClient(config)
    session = db_client.get_async_session()
    res = await update_post_train_data_test(
        session, 16, toxic=1, severe_toxic=0, obscene=1, threat=0, insult=1,
        identity_hate=1, status_id=PostTrainDataStatusID.PROCESSED.value)
    print(res)

    # db_client = SocialMediaDbClient(config)
    # session = db_client.get_async_session()
    # res = await get_post_train_data_by_status_test(
    #     session, PostTrainDataStatusID.NEW.value)
    # print(res)

    # db_client = SocialMediaDbClient(config)
    # session = db_client.get_async_session()
    # await delete_post_train_data_by_id_test(session, 3)