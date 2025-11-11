from app.service.stock_service import stock_service

from tests.test_initapp import registerapp

def test_stock_service_get_kline(registerapp):
    stock_service.get_kline("sh.600519", "2025-09-01", "2025-10-31")
