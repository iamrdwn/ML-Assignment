from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from src.api.middleware.timer import apiTimer
from src.api.routes import router

app = FastAPI()


def init_application():
  _app = FastAPI(title='ML Assignment for Stable Diffusion API')
  _app.add_middleware(apiTimer)
  _app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
  )

  _app.include_router(router)

  return _app
