from fastapi import FastAPI

from .routers import diseases_routes

app = FastAPI()

#app.include_router(users_route.router, prefix=settings.API_V1_STR)
app.include_router(diseases_routes.diseases_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
