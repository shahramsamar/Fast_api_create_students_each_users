from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.responses import JSONResponse
from typing import Optional, List
from sqlalchemy.orm import Session
from database.database import get_db, settings
from models import StudentModel, UserModel
from schemas import *
from auth.utils import authenticate_user, generate_jwt_tokens, generate_access_token
import jwt
from datetime import datetime

router = APIRouter(prefix="/api/v1", tags=["Authenticate with jwt"])


@router.post("/login", 
             response_model=LoginResponseSchema, 
             status_code=status.HTTP_200_OK)
async def login(request : LoginRequestSchema,
                db : Session = Depends(get_db)):
    user = authenticate_user(db,
                             username=request.username,
                             password=request.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="username or password doesn't match")

    jwt_tokens = generate_jwt_tokens(user)
    return {
        "detail": "successfully logged in",
        "access_token": jwt_tokens["access_token"],
        "refresh_token": jwt_tokens["refresh_token"],
        "user_id": user.id
    }


@router.post("/refresh",
             response_model=RefreshResponseSchema,
             status_code=status.HTTP_200_OK)
async def refresh_token(request: RefreshRequestSchema,
                        db: Session = Depends(get_db)):
    token = request.refresh_token
    try:
        result = jwt.decode(token, settings.SECRET_KEY, 
                            algorithms=["HS256"])
        expiration_time = datetime.fromtimestamp(result["exp"]).astimezone()

        if expiration_time < datetime.now().astimezone():
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Invalid token or expired token. (exp)")
        if result["token_type"] != "refresh":
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Invalid token type.")

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"Invalid or expired token. {e}")

    user_obj = db.query(UserModel).filter(UserModel.id == result["user_id"]).one_or_none()
    if not user_obj:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="User does not exist")

    payload = {
        "user_id": user_obj.id,
        "iat": datetime.now().astimezone()
    }

    return {"access_token": generate_access_token(payload)}
