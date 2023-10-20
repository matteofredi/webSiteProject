from fastapi import Request, APIRouter
from fastapi.responses import JSONResponse
from starlette.templating import Jinja2Templates

from main import get_settings

templates = Jinja2Templates(directory='app/static/templates')

router = APIRouter(tags=['FRONTEND'])


@router.get(path='/login', status_code=200)
def login_form(request: Request):
    return templates.TemplateResponse('login-form.html', {'request': request})


@router.get(path='/home', status_code=200)
def home(request: Request):
    return templates.TemplateResponse('home.html', {'request': request})


@router.get(path='/logout', status_code=200)
def logout():
    return JSONResponse(content=f'{get_settings().APP_BASE_URL}/login')
