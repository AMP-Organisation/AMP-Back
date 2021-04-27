from fastapi import FastAPI
from .core.settings import settings
from .routers.users_route import user_router
from .routers.login_route import login_router
from .routers import diseases_routes
from .routers.place_route import place_router
from .routers.symptoms_routes import symptoms_router
from .routers.pillbox_routes import pillbox_router
from .routers.treatment_routes import treatment_router
from fastapi.middleware.cors import CORSMiddleware
from .routers.medicine_routes import medicine_router

app = FastAPI()

app.include_router(user_router, prefix=settings.API_V1_STR)
app.include_router(login_router, prefix=settings.API_V1_STR)
app.include_router(place_router, prefix=settings.API_V1_STR)
app.include_router(diseases_routes.diseases_router, prefix=settings.API_V1_STR)  # peut etre changer l'import. faudra
# rajouter le prefix
app.include_router(symptoms_router, prefix=settings.API_V1_STR)
app.include_router(medicine_router, prefix=settings.API_V1_STR)
app.include_router(pillbox_router, prefix=settings.API_V1_STR)
app.include_router(treatment_router, prefix=settings.API_V1_STR)

# CORS policies
origins = [
    "http://localhost",
    "http://127.0.0.1:8081",
    "http://localhost:8080",  # le front end en localhost
    "https://assistant-medical-personnel.netlify.app"  # le front end en prod
]

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
