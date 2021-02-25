# This is a sample Python script.

from fastapi import FastAPI
from routers import user, information

app = FastAPI()


app.include_router(user.router)
app.include_router(information.router)
