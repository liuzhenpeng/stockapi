# 读取环境变量 ENV，默认使用开发环境
import os
from dotenv import load_dotenv

# 正确导入每个配置类
from app.config.devConfig import devConfig
from app.config.testConfig import testConfig
from app.config.proConfig import proConfig

#加载.env的环境配置
load_dotenv()

env = os.getenv("ENV", "dev")

print(f"当前环境: {env}")
# 根据环境选择配置类
if env == "dev":
    settings = devConfig()
elif env == "test":
    settings = testConfig()
elif env == "pro":
    settings = proConfig()
else:
    raise ValueError(f"不支持的环境: {env}，可选值：dev/test/prod")