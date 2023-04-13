from fastapi import FastAPI, Request, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from scrapper import consultar

app = FastAPI()

origins = [
    "https://railway.app/",
    "https://twitterscrapper-production.up.railway.app/",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="src\\templates")

@app.get('/')
def form_get(request: Request):
    return templates.TemplateResponse("home.html",{"request":request, 'result': 'Resultado...'})

@app.post('/')
def search(request: Request, mensaje: str = Form(...), tipo: str = Form()):
    return templates.TemplateResponse("home.html",{"request":request, 'result': consultar(mensaje)})
