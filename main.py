import uvicorn
from fastapi import FastAPI, Request
from mangum import Mangum
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root(request: Request):
    print(request.headers)
    return {"message": "Hello World"}


@app.get("/aws")
async def aws(request: Request):
    return {"aws": request.scope["aws.event"]}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


handler = Mangum(app)

if __name__ == '__main__':
    uvicorn.run(app)
