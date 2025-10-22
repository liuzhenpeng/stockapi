import pytest
from app.core.register import register_app
from app.api import stock

@pytest.fixture(scope="module")
def registerapp():
    application = register_app()
    yield  application
    stock.bsLogout()