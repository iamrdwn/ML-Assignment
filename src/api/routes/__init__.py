from fastapi import APIRouter
from . import auth
from . import generator

router = APIRouter()

router.include_router(generator.router, tags=['Image Generator'])
