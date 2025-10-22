import pytest
from app.core.register import register_app

@pytest.fixture(scope="module")
def registerapp():
    application = register_app()
    return application