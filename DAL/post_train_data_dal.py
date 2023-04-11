from typing import List, Optional
from sqlalchemy import update, delete
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from sqlalchemy import func
from DAL.social_media_dto import PostTrainData, PostTrainDataStatusID
from DAL.post_data_base_dal import PostDataBase
from datetime import datetime
from enum import IntEnum


class PostTrainDataDAL(PostDataBase):
    
    def __init__(self, db_session: Session):
        super().__init__(db_session)

    async def create_post_train_data(self, 
                                     source: str, 
                                     content: str, 
                                     toxic: Optional[int] = 0,
                                     severe_toxic: Optional[int] = 0,
                                     obscene: Optional[int] = 0,
                                     insult: Optional[int] = 0,
                                     threat: Optional[int] = 0,
                                     identity_hate: Optional[int] = 0) -> PostTrainData:
        new_ptd = PostTrainData(
            source, content, toxic, severe_toxic, obscene, insult, threat, identity_hate,
            status_id = PostTrainDataStatusID.NEW.value, added_on=datetime.utcnow(), 
            last_updated_on=datetime.utcnow())
        self._db_session.add(new_ptd)
        await self._db_session.flush()
        return new_ptd

    async def get_all_post_train_data(self) -> List[PostTrainData]:
        q = await self._db_session.execute(select(PostTrainData).order_by(PostTrainData.id))
        return q.scalars().all()
    
    async def get_post_train_data_by_source(self, source: str) -> List[PostTrainData]:
        q = await self._db_session.execute(
            select(PostTrainData)
           .where(func.lower(PostTrainData.source) == source.lower()))
        return q.scalars().all()
    
    async def get_post_train_data_by_status(self, status_id: int, limit: int = 10) -> PostTrainData:
        q = await self._db_session.execute(
            select(PostTrainData).where(PostTrainData.status_id == status_id).limit(limit))
        return q.scalars().all()

    async def get_post_train_data_by_id(self, id: int) -> PostTrainData:
        q = await self._db_session.execute(
            select(PostTrainData).where(PostTrainData.id == id))
        return q.scalars().first()

    async def delete_post_train_data_by_id(self, id: int) -> None:
        q = delete(PostTrainData).where(PostTrainData.id == id)
        q.execution_options(synchronize_session="fetch")
        await self._db_session.execute(q)

    async def update_post_train_data_by_id(self, 
                                           id: int, 
                                           source: Optional[str] = '',
                                           content: Optional[str] = '',
                                           toxic: Optional[int] = -1,
                                           severe_toxic: Optional[int] = -1,
                                           obscene: Optional[int] = -1,
                                           threat: Optional[int] = -1,
                                           insult: Optional[int] = -1,
                                           identity_hate: Optional[int] = -1,
                                           status_id: Optional[int] = -1) -> bool:
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
        if status_id != -1:
            q = q.values(status_id = status_id)
            is_updated = True

        if is_updated:
            q = q.values(last_updated_on = datetime.utcnow())
            q.execution_options(synchronize_session="fetch")
            await self._db_session.execute(q)
            return True
        return False
    

class PredValsIndex(IntEnum):
    TOXIC = 0,
    SEVERE_TOXIC = 1,
    OBSCENE = 2,
    THREAT = 3,
    INSULT = 4,
    IDENTITY_HATE = 5