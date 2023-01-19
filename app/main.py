from fastapi import FastAPI
from .services.home_service import home_router
from .services.user_service import user_router

from .database.models.users import User
from .database.connection import database

from app import __project_name__, __version__


def include_router(app):
    app.include_router(home_router)
    app.include_router(user_router)


def create_tables(): 
    User.Meta.metadata.create_all(database.engine)


def start_application():
    app = FastAPI(title=__project_name__, version=__version__)
    include_router(app)
    return app


app = start_application()
