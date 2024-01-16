import uvicorn
import logging
from logstash_async.handler import AsynchronousLogstashHandler
from fastapi import FastAPI
from src.routers import hello_world, todos


def get_application() -> FastAPI:
    application = FastAPI()
    application.include_router(hello_world.router)
    application.include_router(todos.router)
    logger.info("Hello world! Api is started.")
    return application


logger = logging.getLogger("no-context-api-logs")
logger.setLevel(logging.INFO)
logstash_handler = AsynchronousLogstashHandler("localhost", 5000, database_path=None)
logger.addHandler(logstash_handler)

app = get_application()

if __name__ == "__main__":
    uvicorn.run("main:app")
    