from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from configparser import ConfigParser


class SocialMediaDbClient():

    def __init__(self):
        config = ConfigParser()
        config.read("Data\\local.ini")
        self.__connection_str = config.get('MySQL', 'ConnectionStr')
        self.__engine = create_async_engine(self.__connection_str, future=True, echo=True)
        self.__async_session = sessionmaker(bind=self.__engine, expire_on_commit=False, class_=AsyncSession)
        self.__base = declarative_base()
    
    async def __del__(self) -> None:
        await self.__engine.dispose()

    def get_engine(self):
        return self.__engine
    
    def get_async_session(self):
        return self.__async_session
    
    def get_base(self):
        return self.__base