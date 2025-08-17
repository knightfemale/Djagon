from ninja import Router

router: Router = Router()

@router.get("/hello")
def hello(request) -> str:
    return "Hello World!"
