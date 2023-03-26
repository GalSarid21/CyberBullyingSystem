from sqlalchemy import Column, Integer, String, DateTime
from DbWriter.db_clients import SocialMediaDbClient

client = SocialMediaDbClient()

class PostTrainData(client.get_base()):
    __tablename__ = 'post_train_data'

    id = Column('id', Integer, primary_key=True)
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

    # def __init__(self):
    
    def __repr__(self) -> str:
        self_str_parts = []
        zipped = zip(self.__dict__.keys(), self.__dict__.values())

        for k, v in zipped:
            self_str_parts.append(f'{k}: {v}')
        
        return ' | '.join(self_str_parts) 