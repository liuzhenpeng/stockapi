from pathlib import Path
from pydantic.v1 import BaseSettings

# 项目根目录
BASE_PATH = Path(__file__).resolve().parent.parent

# 日志文件路径
LOG_DIR = BASE_PATH / 'logs'

# 国际化文件目录
LOCALE_DIR = BASE_PATH / 'locale'

class MyBaseSettings(BaseSettings):
   pass