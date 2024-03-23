from fastapi import FastAPI
from app.containers import Containers
from app.auth import endpoint as auth_endpoints
from app.core import cookies
import asyncio

import uvicorn

app = FastAPI()

def create_app() -> None:
    uvicorn.run(app)


if __name__ =="__main__":
    asyncio.run(create_app())
else:
    uvicorn.run(app)
