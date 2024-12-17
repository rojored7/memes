from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()

# Configuración de carpetas estáticas y plantillas
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Datos de ejemplo
MEMES = [
    {"src": "images/meme1.jpg", "alt": "Meme 1", "link": "https://example1.com"},
    {"src": "images/meme2.jpg", "alt": "Meme 2", "link": "https://example2.com"},
]

SOCIAL_LINKS = {
    "Twitter": "https://twitter.com/example",
    "Instagram": "https://instagram.com/example",
    "Facebook": "https://facebook.com/example"
}

# Ruta principal
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "memes": MEMES, "social_links": SOCIAL_LINKS})
