import functools

from fastapi import FastAPI, staticfiles
from fastapi.responses import RedirectResponse
from starlette.middleware.cors import CORSMiddleware

from api import routers
from core.settings import settings

app = FastAPI()

app.mount('/static', staticfiles.StaticFiles(directory='app/static'), name='static')


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@functools.lru_cache
def get_settings():
    return settings


@app.get(path='/', status_code=200)
def root():
    return RedirectResponse(url=f'{get_settings().APP_BASE_URL}/login')


@app.post(path='/login', status_code=200)
def login(payload: dict):
    return payload


app.include_router(routers.router)
