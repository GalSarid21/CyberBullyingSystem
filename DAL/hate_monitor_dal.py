from datetime import datetime
from sqlalchemy import func
from sqlalchemy import delete
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from typing import Iterable, Optional
from DAL.social_media_dto import HateMonitor


class HateMonitorDAL():
    
    def __init__(self, db_session: Session):
        self._db_session = db_session

    async def create_hate_monitor(self, 
                                  source: str,
                                  user_name: str, 
                                  content: str, 
                                  toxic: Optional[int] = 0,
                                  severe_toxic: Optional[int] = 0,
                                  obscene: Optional[int] = 0,
                                  insult: Optional[int] = 0,
                                  threat: Optional[int] = 0,
                                  identity_hate: Optional[int] = 0) -> HateMonitor:
        new_hm = HateMonitor(
            source, user_name, content, toxic, severe_toxic, 
            obscene, insult, threat, identity_hate,
            added_on=datetime.utcnow(), 
            last_updated_on=datetime.utcnow())
        self._db_session.add(new_hm)
        await self._db_session.flush()
        return new_hm

    async def get_hate_monitors_by_user_name(self, user_name: str) -> Iterable[HateMonitor]:
        q = await self._db_session.execute(
            select(HateMonitor)
           .where(func.lower(HateMonitor.user_name) == user_name.lower()))
        return q.scalars().all()
    
    async def delete_hate_monitor_by_id(self, id: int) -> None:
        q = delete(HateMonitor).where(HateMonitor.id == id)
        q.execution_options(synchronize_session="fetch")
        await self._db_session.execute(q)