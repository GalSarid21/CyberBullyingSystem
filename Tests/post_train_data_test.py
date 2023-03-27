import asyncio
import Tests.app_test as at
from DbWriter.post_train_data_dal import PostTrainDataDAL
from DbWriter.db_clients import SocialMediaDbClient

    
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
                                      identity_hate = -1):
    async with async_session() as session:
        async with session.begin():
            ptd_dal = PostTrainDataDAL(session)
            return await ptd_dal.update_post_train_data_by_id(
                id, source, content, toxic, severe_toxic, obscene, insult, threat, identity_hate)


def run_post_train_data_tests():
    db_client = SocialMediaDbClient()
    session = db_client.get_async_session()
    res = asyncio.run(get_all_post_train_data_test(session))
    print(res)
    
    db_client = SocialMediaDbClient()
    session = db_client.get_async_session()
    res = asyncio.run(get_post_train_data_by_source_test(session, 'twitter'))
    print(res)

    db_client = SocialMediaDbClient()
    session = db_client.get_async_session()
    res = asyncio.run(get_post_train_data_by_id_test(session, 1))
    print(res.id)

    db_client = SocialMediaDbClient()
    session = db_client.get_async_session()
    res = asyncio.run(create_new_post_train_data_test(
        session, 'twitter', 
        'Totally fed up with the way this country has turned into a haven for terrorists. Send them all back home.',
        1, 0, 0, 0, 1, 0))
    print(res.id)

    db_client = SocialMediaDbClient()
    session = db_client.get_async_session()
    res = asyncio.run(update_post_train_data_test(
        session, 3, 'twitter'))
    print(res)

    db_client = SocialMediaDbClient()
    session = db_client.get_async_session()
    asyncio.run(delete_post_train_data_by_id_test(session, 3))