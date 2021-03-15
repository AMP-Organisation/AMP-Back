from fastapi import FastAPI
from core.settings import settings
from app.routers import users_route


app = FastAPI()

app.include_router(users_route.router, prefix=settings.API_V1_STR)


@app.get("/")
def read_root():
    return {"Hello": "World"}
