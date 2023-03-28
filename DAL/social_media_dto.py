from sqlalchemy import Column, Integer, String, DateTime
from DAL.db_clients import SocialMediaDbClient

client = SocialMediaDbClient()
Base = client.get_base()


class PostTrainData(Base):
    __tablename__ = 'post_train_data'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    source = Column('source', String, primary_key=False)
    content = Column('content', String, primary_key=False)
    toxic = Column('toxic', Integer, primary_key=False)
    severe_toxic = Column('severe_toxic', Integer, primary_key=False)
    obscene = Column('obscene', Integer, primary_key=False)
    insult = Column('insult', Integer, primary_key=False)
    threat = Column('threat', Integer, primary_key=False)
    identity_hate = Column('identity_hate', Integer, primary_key=False)
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
        self.added_on = added_on
        self.last_updated_on = last_updated_on

    def __repr__(self) -> str:
        self_str_parts = []
        zipped = zip(self.__dict__.keys(), self.__dict__.values())

        for k, v in zipped:
            self_str_parts.append(f'{k}: {v}')
        
        return ' | '.join(self_str_parts)


class PostPresentationData(Base):
    __tablename__ = 'post_presentation_data'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    source = Column('source', String, primary_key=False)
    content = Column('content', String, primary_key=False)
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
        self_str_parts = []
        zipped = zip(self.__dict__.keys(), self.__dict__.values())

        for k, v in zipped:
            self_str_parts.append(f'{k}: {v}')
        
        return ' | '.join(self_str_parts)