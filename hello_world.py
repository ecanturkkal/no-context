import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get("/hello_world/")
async def hello_world():
    return "Hello World"


@app.on_event("startup")
async def startup():
    pass


@app.on_event("shutdown")
async def shutdown():
    pass


if __name__ == "__main__":
    uvicorn.run("hello_world:app")
