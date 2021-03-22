from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import diseases_routes

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080", # le front end
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#app.include_router(users_route.router, prefix=settings.API_V1_STR)
app.include_router(diseases_routes.diseases_router) # faudra rajouter le prefix

@app.get("/")
def read_root():
    return {"Hello": "World"}
