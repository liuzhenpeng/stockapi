from typing import List

from sqlalchemy_crud_plus import CRUDPlus
from sqlalchemy.ext.asyncio import AsyncSession

from app.model.kduser import User


class CRUDUser(CRUDPlus[User]):
    async def get(self, db: AsyncSession, pk: int) -> User | None:
        """
        获取用户详情

        :param db: 数据库会话
        :param user_id: 用户 ID
        :return:
        """
        return await self.select_model(db, pk)

    async def get_by_tid_uid(self, db: AsyncSession, tid: int, uid: int, limit: int = 20) -> List[User] | None:
        """
        获取用户详情

        :param db: 数据库会话
        :param user_id: 用户 ID
        :return:
        """
        return await self.select_models_order(db, "id", "desc", limit=limit, tid=tid, uid=uid)



userDao: CRUDUser = CRUDUser(User)
