# region Imports
import asyncio
import sqlalchemy as sa
import sqlalchemy.ext.automap as automap
import sqlalchemy.ext.asyncio as sa_asyncio
import sqlalchemy.orm as orm 
# endregion

class MySqlClient():

    def __init__(self, connection_str: str) -> None:
        self.__connection_str = connection_str
        self.__async_engine = sa_asyncio.create_async_engine(
            self.__connection_str, echo=True, future=True, connect_args={'ssl': False})
    

    async def __aexit__(self):
        await self.__async_engine.dispose()


    async def get_all_train_data(self) -> list[sa.Row]:
      async with self.__async_engine.begin() as conn:
        post_train_data = await self.__get_post_train_data_table(conn)
        
        async with self.__async_engine.connect() as conn:
            result = await conn.execute(sa.select(post_train_data))
        return result.fetchall()
      

    async def get_train_data_by_id(self, id: int) -> sa.Row:
      async with self.__async_engine.begin() as conn:
        post_train_data = await self.__get_post_train_data_table(conn)
        
        async with self.__async_engine.connect() as conn:
            result = await conn.execute(
               sa.select(post_train_data)
                 .filter(post_train_data.id == id))
        return result.fetchall()


    async def __get_post_train_data_table(self, conn: sa_asyncio.AsyncConnection) -> sa.Table:
       return await conn.run_sync(lambda conn: sa.Table(
           'post_train_data', sa.MetaData(), 
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('source', sa.String, primary_key=False),
            sa.Column('content', sa.String, primary_key=False),
            sa.Column('toxic', sa.Integer, primary_key=False),
            sa.Column('severe_toxic', sa.Integer, primary_key=False),
            sa.Column('obscene', sa.Integer, primary_key=False),
            sa.Column('insult', sa.Integer, primary_key=False),
            sa.Column('identity_hate', sa.Integer, primary_key=False),
            sa.Column('added_on', sa.DateTime, primary_key=False),
            sa.Column('last_updated_on', sa.DateTime, primary_key=False),
            autoload_with=conn))


    # def create_db_connection(self):
    #     engine = db.create_engine(self.__connection_str)
    #     base = automap.automap_base()
    #     engine = db.create_engine(self.__connection_str)
    #     base.prepare(autoload_with=engine)
    #     post_train_data = base.classes.post_train_data
    #     with orm.Session(engine) as session:
    #         ptd = session.query(post_train_data).first()
    #         print (ptd)
    #         b=3