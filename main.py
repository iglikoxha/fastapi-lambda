from fastapi import FastAPI
from mangum import Mangum
from starlette.requests import Request

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/aws")
async def aws(request: Request):
    return {"aws": request.scope["aws.event"]}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

handler = Mangum(app, lifespan="off")
