import vk_api.exceptions
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from api.vk_apps import *
from fastapi.responses import RedirectResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/')
def render_main_page(request: Request):
    return templates.TemplateResponse("main_page.html", {'request': request})


@app.post(path='/inter_user_analyzez')
async def get_body(request: Request, login=Form(...), password=Form(...)):
    try:
        access_token = get_access_token(login, password)
        return templates.TemplateResponse("inter_user_analyzez.html",
                                          {'request': request, 'access_token': access_token})
    except:
        return RedirectResponse('/')


@app.post(path='/posts')
async def get_posts(request: Request, access_token=Form(...), link=Form(...), quantity=Form(...)):
    object_analis = link.split('/')[-1]
    if object_analis[0:2] == 'id' and object_analis[2] is int:
        data = get_massage_in_wall(access_token, object_analis, count=quantity)
        return templates.TemplateResponse("posts.html",
                                          {'request': request, 'data': data})
    else:
        object_analis = get_user_id(access_token, object_analis)
        data = get_massage_in_wall(access_token, object_analis, count=quantity)
        return templates.TemplateResponse("posts.html",
                                          {'request': request, 'data': data})
