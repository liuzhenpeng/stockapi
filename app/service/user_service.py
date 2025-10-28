from sqlalchemy.ext.asyncio import AsyncSession

from app.models import user_dao
from app.common.exception import errors
from app.model.kduser import User
from app.models.user_dao import userDao


class UserService:
    """用户服务类"""
    @staticmethod
    async def get_fileinfo(*, db: AsyncSession, id: int | None = None, username: str | None = None) -> User:
        """
        获取用户信息

        :param db: 数据库会话
        :param pk: 用户 ID
        :param username: 用户名
        :return:
        """
        file = await userDao.get(db, id=id)
        if not file:
            raise errors.NotFoundError(msg='文件不存在')
        return file

user_service: UserService = UserService()

