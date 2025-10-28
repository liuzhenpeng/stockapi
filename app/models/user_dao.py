from sqlalchemy_crud_plus import CRUDPlus
from sqlalchemy.ext.asyncio import AsyncSession

from app.model.kduser import User

class CRUDUser(CRUDPlus[User]):
    async def get(self, db: AsyncSession, id: int) -> User | None:
        """
        获取用户详情

        :param db: 数据库会话
        :param user_id: 用户 ID
        :return:
        """
        return await self.select_model(db, id)


userDao: CRUDUser = CRUDUser(User)