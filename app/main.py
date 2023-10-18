from fastapi import FastAPI, staticfiles
from fastapi.responses import HTMLResponse, RedirectResponse
from starlette.middleware.cors import CORSMiddleware

from api import routers

app = FastAPI()

app.mount('/static', staticfiles.StaticFiles(directory='app/static'), name='static')


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(path='/', status_code=200)
def root():
    return RedirectResponse(url='http://localhost:8000/login')


@app.post(path='/login', status_code=200)
def login(payload: dict):
    return payload


app.include_router(routers.router)
