from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import requests

app = FastAPI()
templates = Jinja2Templates(directory="templates")

BACKEND_URL = "http://backend:8003"

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/search")
def search(request: Request, question: str = Form(...)):
    resp = requests.get(f"{BACKEND_URL}/search", params={"question": question})
    return templates.TemplateResponse("index.html", {"request": request, "result": resp.json()})

@app.post("/add")
def add(request: Request, data_line: str = Form(...)):
    resp = requests.post(f"{BACKEND_URL}/add", json={"data_line": data_line})
    return templates.TemplateResponse("index.html", {"request": request, "status": resp.json()})

@app.get("/schema")
def schema(request: Request):
    resp = requests.get(f"{BACKEND_URL}/schema_summary")
    return templates.TemplateResponse("index.html", {"request": request, "schema": resp.json()})
