from DAL.hate_monitor_dal import HateMonitorDAL
from DAL.db_clients import SocialMediaDbClient
from configparser import ConfigParser


async def get_hate_monitors_by_user_name_test(async_session, user_name):
    async with async_session() as session:
        async with session.begin():
            hm_dal = HateMonitorDAL(session)
            return await hm_dal.get_hate_monitors_by_user_name(user_name)
        
async def create_new_hate_monitor_test(async_session, 
                                       source, 
                                       user_name,
                                       content, 
                                       toxic, 
                                       severe_toxic, 
                                       obscene, 
                                       insult, 
                                       threat, 
                                       identity_hate):
    async with async_session() as session:
        async with session.begin():
            hm_dal = HateMonitorDAL(session)
            return await hm_dal.create_hate_monitor(
                source, user_name, content, toxic, severe_toxic, 
                obscene, insult, threat, identity_hate)
        
async def delete_hate_monitor_by_id_test(async_session, id):
    async with async_session() as session:
        async with session.begin():
            hm_dal = HateMonitorDAL(session)
            await hm_dal.delete_hate_monitor_by_id(id)
        

async def run_hate_monitor_tests():
    config = ConfigParser()
    config.read("Data\\local.ini")

    try:
        # *** Create new Hate Monitor Test ***
        # db_client = SocialMediaDbClient(config)
        # session = db_client.get_async_session()
        # res = await create_new_hate_monitor_test(
        #     session, 'twitter', 'Ruby M. Perdue',
        #     "Being a DAD means always being a shoulder to cry on",
        #     0, 0, 0, 0, 0, 0)
        # print(res)

        # *** Get Hate Monitor By User Name Test ***
        db_client = SocialMediaDbClient(config)
        session = db_client.get_async_session()
        res = await get_hate_monitors_by_user_name_test(session, 'Ruby M. Perdue')
        print(res)

        # *** Delete Hate Monitor Test ***
        # db_client = SocialMediaDbClient(config)
        # session = db_client.get_async_session()
        # await delete_hate_monitor_by_id_test(session, 0)
    
    except Exception as e:
        print(e)