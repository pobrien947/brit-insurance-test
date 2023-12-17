from fastapi import APIRouter, Request
from app.handler.auth import process_login_data, process_signup_data


router = APIRouter()


@router.post("/login")
async def process_login(request: Request):
    return await process_login_data(request)


@router.post("/signup")
async def process_signup(request: Request):
    return await process_signup_data(request)
