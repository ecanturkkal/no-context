from fastapi import APIRouter


router = APIRouter(prefix="/hello_world")


@router.get("/")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
        