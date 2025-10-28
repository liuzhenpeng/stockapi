import  pytest
from app.api import stock
import matplotlib.pyplot as plt
from tests.test_initapp import registerapp

import pandas as pd

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


def test_Series():
    # 示例数据
    data = {'Category': ['A', 'B', 'C', 'D'],
            'Value': [10, 15, 7, 12]}
    df = pd.DataFrame(data)

    # 绘制饼图
    df.plot(kind='pie', y='Value', labels=df['Category'], autopct='%1.1f%%', title='Category Proportions',
            figsize=(8, 5))
    plt.show()