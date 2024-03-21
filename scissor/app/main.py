from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware


from .templates import templates
from .database import models
from .database.db import engine
from .routers.url import url_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Initialize Jinja2 templates
templates = Jinja2Templates(directory="app/templates")


app.include_router(url_router)
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/")
async def home(request: Request):

    return templates.TemplateResponse("index.html", {"request": request})