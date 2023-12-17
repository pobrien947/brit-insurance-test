from fastapi import Request, HTTPException
from app.config.config import config
from app.model.db import Database
from app.model.user import User
from app.model.basket import Basket
from app.model.item import Item


async def get_user_basket_data(request: Request):
    """
    Get the User's basket
    If they haven't got a basket then return a default one
    :param request:
    :return:
    """
    db = Database(config)
    auth_token, user = authenticate_token(request, db)

    # Has this user already got a basket
    # if not then create a default one
    basket = db.db_session.query(Basket).filter(Basket.user_id == user.id)
    if basket.count() < 1:
        basket = create_new_basket(db, user.id)

    # Create the list of items in the basket
    user_basket = []
    for item in basket:
        user_basket.append(
            {
                "item_name": item.item_name,
                "item_price": item.price,
            }
        )

    return {"data": empty_basket, "auth-token": auth_token}


async def process_basket_summary_data(request: Request):
    """
    Process the basket date and return the summary total
    :param request:
    :return: data summary
    """
    db = Database(config)
    auth_token, user = authenticate_token(request, db)
    request_data = await request.json()

    # delete existing basket for this user
    db.db_session.query(Basket).filter(Basket.user_id == user.id).delete()
    db.db_session.commit()

    # update the basket
    for item in request_data:
        new_basket = Basket(
            user_id=user.id,
            item_name=item["item_name"],
            price=item["item_price"],
        )
        db.db_session.add(new_basket)
        db.db_session.commit()

    # sum the items in the basket
    total = 0
    for item in request_data:
        total = total + item["item_price"]
    summary = {"total": total}

    return {"data": summary, "auth-token": auth_token}


def create_new_basket(db, user_id):
    """
    Create a new basket for a user
    :param db:
    :param user_id:
    :return: basket
    """
    items = db.db_session.query(Item)

    for item in items:
        new_basket = Basket(
            user_id=user_id,
            item_name=item.item_name,
            price=item.default_price,
        )
        db.db_session.add(new_basket)
        db.db_session.commit()

    basket = db.db_session.query(Basket).filter(Basket.user_id == user_id)

    return basket


def authenticate_token(request: Request, db):
    """
    Authenticate token
    TODO: In practice this token would expire after user
          and a new one generated here
    TODO: This function should be moved out into a wider
          helper class for use by all handlers
    :param request:
    :param db:
    :return:
    """
    auth_token = request.headers.get('auth-token')
    if auth_token is None:
        raise HTTPException(status_code=401, detail="Unauthorized")

    # Get the user from the auth-token
    user = db.db_session.query(User).filter(User.auth_token == auth_token)
    if user.count() < 1:
        raise HTTPException(status_code=401, detail="Unauthorized")

    return auth_token, user[0]
