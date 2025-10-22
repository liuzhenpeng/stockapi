import uvicorn

from core.register import register_app

application = register_app()

if __name__ == "__main__":
    uvicorn.run(application, host="0.0.0.0", port=8000)

