import uvicorn

from app.api import stock
from core.register import register_app

application = register_app()

if __name__ == "__main__":
    stock.bsLogin()
    uvicorn.run(application, host="0.0.0.0", port=8000)

