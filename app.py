from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import qrcode
import os

app = FastAPI()

os.makedirs("static", exist_ok=True)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html", context={"qr_generated": False})

@app.post("/", response_class=HTMLResponse)
async def generate(request: Request, data: str = Form(...)):
    qr = qrcode.make(data)
    qr.save("static/qrcode.png")
    return templates.TemplateResponse(request=request, name="index.html", context={"qr_generated": True})