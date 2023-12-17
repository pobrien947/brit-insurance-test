from fastapi import APIRouter, Request
from app.handler.basket import get_user_basket_data, process_basket_summary_data


router = APIRouter()


@router.get("/")
async def process_basket(request: Request):
    return await get_user_basket_data(request)


@router.post("/summary")
async def process_basket_summary(request: Request):
    return await process_basket_summary_data(request)

