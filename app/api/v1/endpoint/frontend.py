from fastapi import Request, APIRouter
from fastapi.responses import JSONResponse
from starlette.templating import Jinja2Templates

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
    return JSONResponse(content='http://localhost:8000/login')
