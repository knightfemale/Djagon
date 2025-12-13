# backend/api.py
from ninja_extra import NinjaExtraAPI


from core.endpoints import router as core_router
from utils.exception_util import register_exception_handlers


api: NinjaExtraAPI = NinjaExtraAPI()

# 注册全局异常处理器
register_exception_handlers(api)

# 注册路由
api.add_router("/", core_router)
