import pytest

from app.models.db import async_db_session
from app.models.user_dao import userDao
from tests.test_initapp import registerapp


@pytest.mark.asyncio
async def test_userdao_get(registerapp):
    print("\n")
    async with async_db_session() as session:
        result = await userDao.get(db=session, pk=1)
        print("获取到的数据：", result)


@pytest.mark.asyncio
async def test_userdao_get_by_tid_uid(registerapp):
    print("\n")
    async with async_db_session() as session:
        result = await userDao.get_by_tid_uid(db=session, tid=10109, uid=92305980)
        if result :
            for item in result:
                print(item)
        else:
            print("没有数据")

