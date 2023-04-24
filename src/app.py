from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from scrapper import search_user, explore, search_tweet
from os.path import dirname, join

app = FastAPI()

current_dir = dirname(__file__)
templates_dir = join(current_dir, "templates")
templates = Jinja2Templates(directory=templates_dir)


@app.get("/")
def form_get(request: Request):
    return templates.TemplateResponse(
        "home.html", {"request": request, "result": "Resultado..."}
    )


@app.post("/")
def search(request: Request, message: str = Form(...), type: str = Form()):
    return templates.TemplateResponse(
        "home.html", {"request": request, "result": search_user(message)}
    )


@app.get("/api/explore")
def explore_tweets():
    return {"response": explore()}


@app.get("/api/user/{user_name}")
def find_user(user_name: str):
    return {"response": search_user(user_name)}


@app.get("/api/tweet/{user_name}/{status}")
def find_tweet(user_name: str, status: str):
    return {"response": search_tweet(user_name, status)}
