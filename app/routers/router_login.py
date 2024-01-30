from fastapi import APIRouter, HTTPException, Request, Response, Depends
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.encoders import jsonable_encoder
# Entity
from entity.login import user


router = APIRouter(
    prefix="/api/v1/login"
)

@router.post("/")
async def login(
    user: user
):
    print(user)