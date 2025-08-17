from ninja import NinjaAPI

from core.endpoint import router as test_router

api: NinjaAPI = NinjaAPI()

api.add_router("/", test_router)
