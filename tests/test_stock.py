import  pytest
from app.api import stock
import matplotlib.pyplot as plt

from app.config import settings
from tests.test_initapp import registerapp

import pandas as pd

def test_stock(registerapp):
   print("hahahahahhahah哈")


@pytest.mark.asyncio
async def test_stock_t(registerapp):
    print("\n")
    print(settings.PROJECT_NAME)
    result = await stock.test("黑暗时代是")
    print("获取到的数据：", result)


@pytest.mark.asyncio
async def test_getStocks(registerapp):
    print("\n")
    result = await stock.getStocks()
    print("获取到的数据：", result)

@pytest.mark.asyncio
async def test_queryForecastReport(registerapp):
    print("\n")
    result = await stock.queryForecastReport("sh.600000", "2023-01-01", "2025-12-31")
    print("获取到的数据：", result)

@pytest.mark.asyncio
async def test_queryPerformanceExpressReport(registerapp):
    print("\n")
    result = await stock.queryPerformanceExpressReport("sh.600000", "2023-01-01", "2025-12-31")
    print("获取到的数据：", result)

@pytest.mark.asyncio
async def test_queryProfitData(registerapp):
    print("\n")
    result = await stock.queryProfitData("sh.600000", 2025, 3)
    print("获取到的数据：", result)

def test_Series():
    # 示例数据
    data = {'Category': ['A', 'B', 'C', 'D'],
            'Value': [10, 15, 7, 12]}
    df = pd.DataFrame(data)

    # 绘制饼图
    df.plot(kind='pie', y='Value', labels=df['Category'], autopct='%1.1f%%', title='Category Proportions',
            figsize=(8, 5))
    plt.show()