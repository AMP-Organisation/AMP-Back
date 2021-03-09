from fastapi import FastAPI
from .core.settings import settings
from .routers.place_route import place_router

app = FastAPI()

app.include_router(place_router, prefix=settings.API_V1_STR)


@app.get("/")
def read_root():
    return {"Hello": "World"}
