# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from fastapi import FastAPI
from routers import user, information

app = FastAPI()


app.include_router(user.router)
app.include_router(information.router)
