import logging

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from .settings import settings

"""
FastAPI setup
"""
app = FastAPI()


@app.on_event("startup")
async def app_init():
    # Enable logging. INFO is default. DEBUG if requested
    logging.basicConfig(
        level=logging.DEBUG if settings.debug else logging.INFO,
        format=settings.logformat,
    )
    app.mount("/jsapp", StaticFiles(directory=settings.http_jsapp_dir), name="jsapp")


"""
A blank URL takes us to our JS-app
"""


# @app.get("/", tags=["Root"], include_in_schema=False)
# async def index():
#     return RedirectResponse("/jsapp/index.html")

