# route_homepage.py

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from app import __version__

user_router = APIRouter()


@user_router.get("/")
async def home(request: Request):

    return JSONResponse(
        dict(
            app="User FastAPI",
            version=__version__,
        )
    )
