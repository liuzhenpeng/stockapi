from app.config.base import MyBaseSettings
from typing import Literal

class testConfig(MyBaseSettings):
    # 调试模式
    APP_DEBUG: bool = True
    # 项目信息
    VERSION: str = "0.0.1"
    PROJECT_NAME: str = "fasdapi_test"

    # .env 数据库
    DATABASE_TYPE: Literal['mysql'] = 'mysql'
    DATABASE_HOST: str = '192.168.3.40'
    DATABASE_PORT: int = 3306
    DATABASE_USER: str  = 'root'
    DATABASE_PASSWORD: str = 'Mysql@2018'

    # 数据库
    DATABASE_ECHO: bool | Literal['debug'] = False
    DATABASE_POOL_ECHO: bool | Literal['debug'] = False
    DATABASE_SCHEMA: str = 'kdrive'
    DATABASE_CHARSET: str = 'utf8mb4'

    # Session
    SECRET_KEY = "session"
    SESSION_COOKIE = "session_id"
    SESSION_MAX_AGE = 14 * 24 * 60 * 60
    # Jwt
    JWT_SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    JWT_ALGORITHM = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES = 24 * 60

    SWAGGER_UI_OAUTH2_REDIRECT_URL = "/api/v1/test/oath2"

    # 二维码过期时间
    QRCODE_EXPIRE = 60 * 1

    # Trace ID
    TRACE_ID_REQUEST_HEADER_KEY: str = 'X-Request-ID'
    TRACE_ID_LOG_LENGTH: int = 32  # UUID 长度，必须小于等于 32
    TRACE_ID_LOG_DEFAULT_VALUE: str = '-'

    # 日志（控制台）
    LOG_STD_LEVEL: str = 'INFO'

    # 日志（文件）
    LOG_FILE_ACCESS_LEVEL: str = 'INFO'
    LOG_FILE_ERROR_LEVEL: str = 'INFO'
    LOG_ACCESS_FILENAME: str = 'fba_access.log'
    LOG_ERROR_FILENAME: str = 'fba_error.log'

    # 时间配置
    DATETIME_TIMEZONE: str = 'Asia/Shanghai'
    DATETIME_FORMAT: str = '%Y-%m-%d %H:%M:%S'

    # I18n 配置
    I18N_DEFAULT_LANGUAGE: str = 'zh-CN'
    #  BaoStock 登录配置
    BAOSTOCK_LOGIN = False