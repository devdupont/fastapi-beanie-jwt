"""Server app config."""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from starlette.middleware.cors import CORSMiddleware

from myserver.config import CONFIG
from myserver.models.user import User


DESCRIPTION = """
This API powers whatever I want to make

It supports:

- Account sign-up and management
- Something really cool that will blow your socks off
"""


@asynccontextmanager
async def lifespan(app: FastAPI):  # type: ignore
    """Initialize application services."""
    app.db = AsyncIOMotorClient(CONFIG.mongo_uri).account  # type: ignore[attr-defined]
    await init_beanie(app.db, document_models=[User])  # type: ignore[arg-type,attr-defined]
    print("Startup complete")
    yield
    print("Shutdown complete")


app = FastAPI(
    title="My Server",
    description=DESCRIPTION,
    version="0.1.0",
    contact={
        "name": "Hello World Jr",
        "url": "https://myserver.dev",
        "email": "helloworld@myserver.dev",
    },
    license_info={
        "name": "MIT",
        "url": "https://github.com/flyinactor91/fastapi-beanie-jwt/blob/main/LICENSE",
    },
    lifespan=lifespan,
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
