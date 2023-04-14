from fastapi import FastAPI, Request, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from scrapper import consultar
from os.path import dirname, join

app = FastAPI()

current_dir = dirname(__file__) 
templates_dir = join(current_dir, 'templates')
templates = Jinja2Templates(directory=templates_dir)

@app.get('/')
def form_get(request: Request):
    return templates.TemplateResponse("home.html",{"request":request, 'result': 'Resultado...'})

@app.post('/')
def search(request: Request, mensaje: str = Form(...), tipo: str = Form()):
    return templates.TemplateResponse("home.html",{"request":request, 'result': consultar(mensaje)})
