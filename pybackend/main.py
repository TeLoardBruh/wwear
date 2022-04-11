from ast import Str
from typing import Optional
from routes.item import item
from routes.user import user
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(item)
app.include_router(user)

if __name__ == "__main__":
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000, reload=True)