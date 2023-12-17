from uuid import uuid4
from fastapi import Request, HTTPException
from app.config.config import config
from app.model.db import Database
from app.model.user import User


async def process_login_data(request: Request):
    """
    Authenticate a sign in attempt
    :param request:
    :return: token
    """
    request_data = await request.json()

    print(request_data["username"])
    print(request_data["password"])

    db = Database(config)

    # Do we have an entry for this username
    user = db.db_session.query(User).filter(User.username == request_data["username"])
    if user.count() < 1:
        raise HTTPException(status_code=404, detail="User not found")

    # Is the password correct
    if user[0].password != request_data["password"]:
        raise HTTPException(status_code=401, detail="Incorrect Password")

    # Authenticated so generate the user token
    # TODO: in practice the token would expire
    #       after use and new one generated
    user[0].auth_token = uuid4()
    db.db_session.add(user[0])
    db.db_session.commit()

    return {f"token: {user[0].auth_token}"}


async def process_signup_data(request: Request):
    """
    Add a new user
    :param request:
    :return: token
    """
    request_data = await request.json()

    db = Database(config)

    # Do we already have an entry for this username
    user = db.db_session.query(User).filter(User.username == request_data["username"])
    if user.count() > 0:
        raise HTTPException(status_code=401, detail="User already exists")

    # Is the password at least 6 characters
    # TODO: In practice we would add a lot more validation here
    #       making the password conform to a wider set of rules
    #       e.g. min length, Upper case, Lower case, numeric and non alpha
    if len(request_data["password"]) < 6:
        raise HTTPException(status_code=401, detail="Password too short, must be at least 6 characters")

    # Create the user
    new_user = User(username=request_data["username"],
                    password=request_data["password"])
    db.db_session.add(new_user)
    db.db_session.commit()

    return {f"user {new_user.username} has been created"}
