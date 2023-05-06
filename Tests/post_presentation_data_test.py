from DAL.post_presentation_data_dal import PostPresentationDataDAL
from DAL.db_clients import SocialMediaDbClient
from configparser import ConfigParser

async def get_max_post_id_test(async_session):
    async with async_session() as session:
        async with session.begin():
            ptd_dal = PostPresentationDataDAL(session)
            return await ptd_dal.get_max_post_id()

async def get_all_post_presentation_data_test(async_session):
    async with async_session() as session:
        async with session.begin():
            ptd_dal = PostPresentationDataDAL(session)
            return await ptd_dal.get_all_post_presentation_data()
        
async def get_post_presentation_data_by_source_test(async_session, source):
    async with async_session() as session:
        async with session.begin():
            ptd_dal = PostPresentationDataDAL(session)
            return await ptd_dal.get_post_presentation_data_by_source(source)

async def delete_post_presentation_data_by_id_test(async_session, id):
    async with async_session() as session:
        async with session.begin():
            ptd_dal = PostPresentationDataDAL(session)
            return await ptd_dal.delete_post_presentation_data_by_id(id)

async def get_post_presentation_data_by_id_test(async_session, id):
    async with async_session() as session:
        async with session.begin():
            ptd_dal = PostPresentationDataDAL(session)
            return await ptd_dal.get_post_presentation_data_by_id(id)

async def get_post_presentation_data_by_user_name_test(async_session, user_name):
    async with async_session() as session:
        async with session.begin():
            ptd_dal = PostPresentationDataDAL(session)
            return await ptd_dal.get_post_presentation_data_by_user_name(user_name)
        
async def create_new_post_presentation_data_test(async_session, source, content):
    async with async_session() as session:
        async with session.begin():
            ptd_dal = PostPresentationDataDAL(session)
            return await ptd_dal.create_post_presentation_data(source, content)
        
async def update_post_presentation_data_test(async_session, id, source = '', content = '', user_name = ''):
    async with async_session() as session:
        async with session.begin():
            ptd_dal = PostPresentationDataDAL(session)
            return await ptd_dal.update_post_presentation_data_by_id(id, source, content, user_name)


async def run_post_presentation_data_tests():
    config = ConfigParser()
    config.read("Data\\local.ini")
    
    db_client = SocialMediaDbClient(config)
    session = db_client.get_async_session()
    res = await get_max_post_id_test(session)
    print(res)

    db_client = SocialMediaDbClient(config)
    session = db_client.get_async_session()
    res = await get_all_post_presentation_data_test(session)
    print(res)
    
    db_client = SocialMediaDbClient(config)
    session = db_client.get_async_session()
    res = await get_post_presentation_data_by_source_test(session, 'twitter')
    print(res)

    db_client = SocialMediaDbClient(config)
    session = db_client.get_async_session()
    res = await get_post_presentation_data_by_user_name_test(session, 'Ben234')
    print(res)

    db_client = SocialMediaDbClient(config)
    session = db_client.get_async_session()
    res = await get_post_presentation_data_by_id_test(session, 1)
    print(res.id)

    # db_client = SocialMediaDbClient(config)
    # session = db_client.get_async_session()
    # res = await create_new_post_presentation_data_test(
    #     session, 'twitter', 
    #     'Day after long holiday my local bank branch has 47 people in queue and only 2 out of 7 tellers open. Fuck you, Bangkok Bank. #fail',
    #     'test')
    # print(res.id)

    # db_client = SocialMediaDbClient(config)
    # session = db_client.get_async_session()
    # res = await update_post_presentation_data_test(
    #     session, 3, user_name='Ben234')
    # print(res)

    # db_client = SocialMediaDbClient(config)
    # session = db_client.get_async_session()
    # await delete_post_presentation_data_by_id_test(session, 2)