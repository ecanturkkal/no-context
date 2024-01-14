from fastapi import FastAPI
import uvicorn
from routers import todos, hello_world


def get_application() -> FastAPI:
    application = FastAPI()
    application.include_router(hello_world.router)
    application.include_router(todos.router)

    return application


app = get_application()

if __name__ == "__main__":
    uvicorn.run("main:app")
    