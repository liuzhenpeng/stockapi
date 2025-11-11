import baostock as bs
import pandas as pd
from matplotlib import pyplot as plt
import mplfinance as mpf
import plotly.graph_objects as go
from app.utils.log import log
from plotly.subplots import make_subplots


class StockService:
    """用户服务类"""
    @staticmethod
    def get_kline(code: str, start_date: str, end_date: str):
            rs = bs.query_history_k_data_plus(code,
                                              "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,isST",
                                              start_date=start_date, end_date=end_date,
                                              frequency="d", adjustflag="3")
            if rs and rs.error_code != "0":
                # 使用 rs.error_code 作为业务错误码，rs.error_msg 作为错误描述
                return
            else:
                data_list = []
                if rs:
                    while (rs.error_code == '0') & rs.next():
                        # 获取一条记录，将记录合并在一起
                        data_list.append(rs.get_row_data())

                df = pd.DataFrame(data_list, columns=rs.fields)

                # 2. 转换日期为datetime类型，并设为索引（必须步骤）
                df['date'] = pd.to_datetime(df['date'])
                df.set_index('date', inplace=True)

                # 3. 将数值列转换为float类型（修复数据类型错误）
                numeric_columns = ['open', 'high', 'low', 'close', 'preclose', 'volume', 'amount']
                for col in numeric_columns:
                    if col in df.columns:
                        df[col] = pd.to_numeric(df[col], errors='coerce')
                mpf.plot(df,type='candle',mav=(5,10,20),volume=True)




                return



stock_service: StockService =  StockService()