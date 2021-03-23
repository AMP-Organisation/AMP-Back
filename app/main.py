from fastapi import FastAPI

from .core.settings import settings
from .routers.users_route import user_router
from .routers.login_route import login_router
from .routers import diseases_routes
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost",
    "http://localhost:8080", # le front end en localhost

]

app = FastAPI()

app.include_router(user_router, prefix=settings.API_V1_STR)
app.include_router(login_router, prefix=settings.API_V1_STR)
app.include_router(diseases_routes.diseases_router, prefix=settings.API_V1_STR) # peut etre changer l'import. faudra
# rajouter le prefix

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}
