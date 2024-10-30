
from models import UserModel, TokenModel
from datetime import datetime, timezone, timedelta
import random
import string
import jwt
from database.config import settings


def authenticate_user(db, username, password):
    user = db.query(UserModel).filter(UserModel.username == username).first()
    if not user:
        return None
    return user


def generate_token(db, user):
    token = ''.join(random.choices(
        string.ascii_uppercase + string.digits, k=20))
    expiration_time = datetime.now(timezone.utc) + timedelta(days=7)
    existing_token = db.query(TokenModel).filter(
        TokenModel.user_id == user.id).one_or_none()
    if existing_token:
        existing_token.expiration_date = datetime.now(
            timezone.utc) + timedelta(days=7)
        existing_token.token = token
        db.commit()
        db.refresh(existing_token)
    else:
        token_obj = TokenModel(user_id=user.id, 
                               token=token,
                               expiration_date=expiration_time)
        db.add(token_obj)
        db.commit()
        db.refresh(token_obj)
    return token


def generate_access_token(payload):
    payload.update({
        "token_type": "access",
        "exp": datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_EXPIRATION),

    })
    return jwt.encode(payload,
                      settings.SECRET_KEY, 
                      "HS256")


def generate_refresh_token(payload):
    payload.update({
        "token_type": "refresh",
        "exp": datetime.now(timezone.utc) + timedelta(minutes=settings.REFRESH_EXPIRATION),
    })
    return jwt.encode(payload, 
                      settings.SECRET_KEY,
                      "HS256")


def generate_jwt_tokens(user):
    payload = {
        "user_id": user.id,
        "iat": datetime.now(timezone.utc)
    }
    return {
        "access_token": generate_access_token(payload),
        "refresh_token": generate_refresh_token(payload)

    }
