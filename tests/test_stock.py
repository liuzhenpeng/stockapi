import  pytest
from app.api import stock

from tests.test_initapp import registerapp

def test_stock(registerapp):
   print("hahahahahhahah哈")


@pytest.mark.asyncio
async def test_stock_t(registerapp):
    print("\n")
    result = await stock.test("黑暗时代是")
    print("获取到的数据：", result)


@pytest.mark.asyncio
async def test_getStocks(registerapp):
    print("\n")
    result = await stock.getStocks()
    print("获取到的数据：", result)
