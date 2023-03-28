from typing import List, Optional
from sqlalchemy import update, delete
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from sqlalchemy import func
from DAL.social_media_dto import PostPresentationData
from datetime import datetime


class PostPresentationDataDAL():
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def create_post_presentation_data(self, 
                                            source: str, 
                                            content: str,
                                            user: str) -> PostPresentationData:
        new_ppd = PostPresentationData(
            source, content, user, added_on=datetime.utcnow(), last_updated_on=datetime.utcnow())
        self.db_session.add(new_ppd)
        await self.db_session.flush()
        return new_ppd

    async def get_all_post_presentation_data(self) -> List[PostPresentationData]:
        q = await self.db_session.execute(
            select(PostPresentationData).order_by(PostPresentationData.id))
        return q.scalars().all()
    
    async def get_post_presentation_data_by_source(self, source: str) -> List[PostPresentationData]:
        q = await self.db_session.execute(
            select(PostPresentationData)
           .where(func.lower(PostPresentationData.source) == source.lower()))
        return q.scalars().all()
    
    async def get_post_presentation_data_by_id(self, id: int) -> PostPresentationData:
        q = await self.db_session.execute(
            select(PostPresentationData).where(PostPresentationData.id == id))
        return q.scalars().first()

    async def get_post_presentation_data_by_user_name(self, user_name: str) -> List[PostPresentationData]:
        q = await self.db_session.execute(
            select(PostPresentationData)
           .where(func.lower(PostPresentationData.user_name) == user_name.lower()))
        return q.scalars().all()

    async def delete_post_presentation_data_by_id(self, id: int) -> None:
        q = delete(PostPresentationData).where(PostPresentationData.id == id)
        q.execution_options(synchronize_session="fetch")
        await self.db_session.execute(q)

    async def update_post_presentation_data_by_id(self, 
                                                  id: int, 
                                                  source: Optional[str] = '',
                                                  content: Optional[str] = '',
                                                  user_name: Optional[str] = '') -> bool:
        q = update(PostPresentationData).where(PostPresentationData.id == id)
        is_updated = False
        
        if source != '':
            q = q.values(source = source)
            is_updated = True
        if content != '':
            q = q.values(content = content)
            is_updated = True
        if user_name != '':
            q = q.values(user_name = user_name)
            is_updated = True

        if is_updated:
            q = q.values(last_updated_on = datetime.utcnow())
            q.execution_options(synchronize_session="fetch")
            await self.db_session.execute(q)
            return True
        return False