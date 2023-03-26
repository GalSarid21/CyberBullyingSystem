from typing import List, Optional
from sqlalchemy import update, delete
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from DbWriter.social_media_dto import PostTrainData
from datetime import datetime


class PostTrainDataDAL():
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def create_post_train_data(self, 
                                     source: str, 
                                     content: str, 
                                     toxic: int,
                                     severe_toxic: int,
                                     obscene: int,
                                     insult: int,
                                     threat: int,
                                     identity_hate: int) -> PostTrainData:
        new_ptd = PostTrainData(
            source, content, toxic, severe_toxic, obscene, insult, threat, identity_hate,
            added_on=datetime.utcnow(), last_updated_on=datetime.utcnow())
        self.db_session.add(new_ptd)
        await self.db_session.flush()
        return new_ptd

    async def get_all_post_train_data(self) -> List[PostTrainData]:
        q = await self.db_session.execute(select(PostTrainData).order_by(PostTrainData.id))
        return q.scalars().all()
    
    async def get_post_train_data_by_source(self, source: str) -> List[PostTrainData]:
        q = await self.db_session.execute(
            select(PostTrainData).where(PostTrainData.source == source))
        return q.scalars().all()
    
    async def get_post_train_data_by_id(self, id: int) -> PostTrainData:
        q = await self.db_session.execute(
            select(PostTrainData).where(PostTrainData.id == id))
        return q.scalars().first()

    async def delete_post_train_data_by_id(self, id: int) -> None:
        q = delete(PostTrainData).where(PostTrainData.id == id)
        q.execution_options(synchronize_session="fetch")
        await self.db_session.execute(q)

    async def update_post_train_data_by_id(self, 
                                           id: int, 
                                           source: Optional[str] = '',
                                           content: Optional[str] = '',
                                           toxic: Optional[int] = -1,
                                           severe_toxic: Optional[int] = -1,
                                           obscene: Optional[int] = -1,
                                           threat: Optional[int] = -1,
                                           insult: Optional[int] = -1,
                                           identity_hate: Optional[int] = -1) -> bool:
        q = update(PostTrainData).where(PostTrainData.id == id)
        is_updated = False
        
        if source != '':
            q = q.values(source = source)
            is_updated = True
        if content != '':
            q = q.values(content = content)
            is_updated = True
        if toxic != -1:
            q = q.values(toxic = toxic)
            is_updated = True
        if severe_toxic != -1:
            q = q.values(severe_toxic = severe_toxic)
            is_updated = True
        if obscene != -1:
            q = q.values(obscene = obscene)
            is_updated = True
        if threat != -1:
            q = q.values(threat = threat)
            is_updated = True
        if insult != -1:
            q = q.values(insult = insult)
            is_updated = True
        if identity_hate != -1:
            q = q.values(identity_hate = identity_hate)
            is_updated = True

        if is_updated:
            q = q.values(last_updated_on = datetime.utcnow())
            q.execution_options(synchronize_session="fetch")
            await self.db_session.execute(q)
            return True
        return False