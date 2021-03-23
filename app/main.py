from fastapi import FastAPI
from .core.settings import settings
from .routers.users_route import user_router
from .routers.login_route import login_router


app = FastAPI()

app.include_router(user_router, prefix=settings.API_V1_STR)
app.include_router(login_router, prefix=settings.API_V1_STR)


@app.get("/")
def read_root():
    return {"Hello": "World"}
