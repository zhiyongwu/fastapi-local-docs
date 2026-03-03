import pathlib

from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from .internal import docs, redoc


def create_fastapi_app(root_path='', **kwargs):
    app = FastAPI(root_path=root_path, docs_url=None, redoc_url=None, **kwargs)

    app.mount('/_static', StaticFiles(directory=pathlib.Path(__file__).parent / 'static'), name='_static')
    app.include_router(docs.router)
    app.include_router(redoc.router)
    return app
