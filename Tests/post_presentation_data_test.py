import asyncio
from DbWriter.post_presentation_data_dal import PostPresentationDataDAL
from DbWriter.db_clients import SocialMediaDbClient

    
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
        
async def create_new_post_presentation_data_test(async_session, source, content):
    async with async_session() as session:
        async with session.begin():
            ptd_dal = PostPresentationDataDAL(session)
            return await ptd_dal.create_post_presentation_data(source, content)
        
async def update_post_presentation_data_test(async_session, id, source = '', content = ''):
    async with async_session() as session:
        async with session.begin():
            ptd_dal = PostPresentationDataDAL(session)
            return await ptd_dal.update_post_presentation_data_by_id(id, source, content)


def run_post_presentation_data_tests():
    # db_client = SocialMediaDbClient()
    # session = db_client.get_async_session()
    # res = asyncio.run(get_all_post_presentation_data_test(session))
    # print(res)
    
    # db_client = SocialMediaDbClient()
    # session = db_client.get_async_session()
    # res = asyncio.run(get_post_presentation_data_by_source_test(session, 'twitter'))
    # print(res)

    # db_client = SocialMediaDbClient()
    # session = db_client.get_async_session()
    # res = asyncio.run(get_post_presentation_data_by_id_test(session, 1))
    # print(res.id)

    db_client = SocialMediaDbClient()
    session = db_client.get_async_session()
    res = asyncio.run(create_new_post_presentation_data_test(
        session, 'twitter', 
        'Day after long holiday my local bank branch has 47 people in queue and only 2 out of 7 tellers open. Fuck you, Bangkok Bank. #fail'))
    print(res.id)

    # db_client = SocialMediaDbClient()
    # session = db_client.get_async_session()
    # res = asyncio.run(update_post_presentation_data_test(
    #     session, 2, 'twitter'))
    # print(res)

    # db_client = SocialMediaDbClient()
    # session = db_client.get_async_session()
    # asyncio.run(delete_post_presentation_data_by_id_test(session, 2))