from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from DAL.db_clients import SocialMediaDbClient
from enum import IntEnum

client = SocialMediaDbClient()
Base = client.get_base()


class PostTrainDataStatusID(IntEnum):
    NEW = 1,
    PROCESSING = 2,
    PROCESSED = 3,
    TRAINED = 4,
    FAILED = 5

    def __int__(self):
        return self.value


class PostTrainDataStatus(Base):
    __tablename__ = 'post_train_data_status'

    status_id = Column('id', Integer, primary_key=True)
    status_str = Column('status_str', String, primary_key=False)


class PostTrainData(Base):
    __tablename__ = 'post_train_data'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    source = Column('source', String, primary_key=False)
    content = Column('content', String, primary_key=False, unique=True)
    toxic = Column('toxic', Integer, primary_key=False)
    severe_toxic = Column('severe_toxic', Integer, primary_key=False)
    obscene = Column('obscene', Integer, primary_key=False)
    insult = Column('insult', Integer, primary_key=False)
    threat = Column('threat', Integer, primary_key=False)
    identity_hate = Column('identity_hate', Integer, primary_key=False)
    status_id = Column('status_id', Integer, ForeignKey(PostTrainDataStatus.status_id), primary_key=False)
    added_on = Column('added_on', DateTime, primary_key=False)
    last_updated_on = Column('last_updated_on', DateTime, primary_key=False)

    def __init__(self, 
                 source: String,
                 content: String,
                 toxic: Integer,
                 severe_toxic: Integer,
                 obscene: Integer,
                 insult: Integer,
                 threat: Integer,
                 identity_hate: Integer,
                 status_id: Integer,
                 added_on: DateTime,
                 last_updated_on: DateTime):
        self.source = source
        self.content = content
        self.toxic = toxic
        self.severe_toxic = severe_toxic
        self.obscene = obscene
        self.insult = insult
        self.threat = threat
        self.identity_hate = identity_hate
        self.status_id = status_id
        self.added_on = added_on
        self.last_updated_on = last_updated_on

    def __repr__(self) -> str:
        obj_str = f'id: {self.id} | source: {self.source}\ncontent: {self.content}\n' +\
                  f'tocix: {self.toxic}, severe toxic: {self.severe_toxic}, obscene: {self.obscene}, ' +\
                  f'insult: {self.insult}, threat: {self.threat}, identity hate: {self.identity_hate}, ' +\
                  f'status id: {self.status_id}, added on: {self.added_on}, last updated on: {self.last_updated_on}'
        return obj_str


class PostPresentationData(Base):
    __tablename__ = 'post_presentation_data'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    source = Column('source', String, primary_key=False)
    content = Column('content', String, primary_key=False, unique=True)
    user_name = Column('user_name', String, primary_key=False)
    added_on = Column('added_on', DateTime, primary_key=False)
    last_updated_on = Column('last_updated_on', DateTime, primary_key=False)

    def __init__(self, 
                 source: String,
                 content: String,
                 user_name: String,
                 added_on: DateTime,
                 last_updated_on: DateTime):
        self.source = source
        self.content = content
        self.user_name = user_name
        self.added_on = added_on
        self.last_updated_on = last_updated_on
    
    def __repr__(self) -> str:
        obj_str = f'id: {self.id} | source: {self.source}\ncontent: {self.content}\n' +\
                  f'user name: {self.user_name}, added on: {self.added_on}, last updated on: {self.last_updated_on}'
        return obj_str
