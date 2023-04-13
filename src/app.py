from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from scrapper import consultar

app = FastAPI()

templates = Jinja2Templates(directory="src\\templates")

@app.get('/')
def form_get(request: Request):
    return templates.TemplateResponse("home.html",{"request":request, 'result': 'Resultado...'})

@app.post('/')
def search(request: Request, mensaje: str = Form(...), tipo: str = Form()):
    return templates.TemplateResponse("home.html",{"request":request, 'result': consultar(mensaje)})
