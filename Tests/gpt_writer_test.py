from configparser import ConfigParser
from DAL.db_clients import SocialMediaDbClient
from DbWriter.gpt_writer import GptWriterEngine
from DAL.post_train_data_dal import PostTrainDataDAL


async def run_gpt_writer_test():
    config = ConfigParser()
    config.read("Data\\local.ini")
    db_client = SocialMediaDbClient(config)
    engine = GptWriterEngine(config, db_client)

    # get labels test
    # res = await engine.get_labels('real question is do feminist liberal bigots understand that different rules fro men/weman is sexism')
    # print(res)

    # write labels test
    try:
        while True:
            await engine.write_labels_to_db()
    except Exception as e:
        print(e)