from fastapi import FastAPI

app = FastAPI()

from routes import auth

app.include_router(auth)