from fastapi import FastAPI

from config.config import settings
from core.router import router

from utils.log import setup_logging, set_custom_logfile


def register_app() -> FastAPI:
    """
     注册app
    :return: FastAPI
    """

    application = FastAPI(
        debug=settings.APP_DEBUG
    )

    #注册路由
    application.include_router(router)
    register_logger()

    return application


def register_logger() -> None:
    """注册日志"""
    setup_logging()
    set_custom_logfile()