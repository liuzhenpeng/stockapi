import baostock as bs
from fastapi import APIRouter

from common.response.response_code import CustomErrorCode, CustomCodeBase, CustomResponse
from utils.log import log
from common.response.response_schema import response_base, ResponseSchemaModel

router = APIRouter(prefix='/baostock')


@router.get("/getKline")
async def getKline(code: str, start_date: str, end_date: str):
    #### 获取沪深A股历史K线数据 ####
    # 详细指标参数，参见“历史行情指标参数”章节；“分钟线”参数与“日线”参数不同。“分钟线”不包含指数。
    # 分钟线指标：date,time,code,open,high,low,close,volume,amount,adjustflag
    # 周月线指标：date,code,open,high,low,close,volume,amount,adjustflag,turn,pctChg
    rs = None
    try:
        rs = bs.query_history_k_data_plus(code,
                                          "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,isST",
                                          start_date=start_date, end_date=end_date,
                                          frequency="d", adjustflag="3")
        if rs and rs.error_code != "0":
            # 使用 rs.error_code 作为业务错误码，rs.error_msg 作为错误描述
            return response_base.fail(res=CustomResponse(code=int(rs.error_code), msg=rs.error_msg))
        else:
            data_list = []
            if rs:
                while (rs.error_code == '0') & rs.next():
                    # 获取一条记录，将记录合并在一起
                    data_list.append(rs.get_row_data())

            return response_base.success(data=data_list)

    except Exception as e:
        log.error(f"获取k线数据失败,code:{code},start_date:{start_date},end_date:{end_date},error:{e}")
        return response_base.fail(res=CustomErrorCode.CAPTCHA_ERROR, data=e)


def bsLogin():
    #### 登陆系统 ####
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:' + lg.error_code)
    print('login respond  error_msg:' + lg.error_msg)


def bsLogout():
    #### 登出系统 ####
    bs.logout()


@router.get("/test")
async def test(code: str):
    log.error(f"你好:{code}")
    return response_base.fail(res=CustomErrorCode.CAPTCHA_ERROR, data=code)
