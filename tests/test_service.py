import pytest

from app.models.db import  async_db_session
from tests.test_initapp import registerapp
from app.service.user_service import user_service



@pytest.mark.asyncio
async def test_userdao_get(registerapp):
    print("\n")
    async with async_db_session() as session:
        result = await user_service.get_fileinfo(db=session, id=1)
        print("获取到的数据：", result)
