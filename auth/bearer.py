from fastapi import Request, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from models import TokenModel, UserModel
from database.database import get_db
import jwt
from database.config import settings
from datetime import datetime, timezone, timedelta


class TokenBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(TokenBearer, self).__init__(auto_error=auto_error)

    async def __call__(self,
                       request: Request,
                       db: Session = Depends(get_db)):
        credentials: HTTPAuthorizationCredentials = await super(TokenBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=401, detail="Invalid authentication scheme.")
            user = self.verify_token(db,
                                     credentials.credentials)
            if not user:
                raise HTTPException(
                    status_code=401,
                    detail="Invalid token or expired token.")
            return user
        else:
            raise HTTPException(
                status_code=401,
                detail="Invalid authorization code.")

    def verify_token(self, db, token: str):
        try:
            result = jwt.decode(token, 
                                settings.SECRET_KEY,
                                "HS256")
            expiration_time = datetime.fromtimestamp(result["exp"]).astimezone()   
                  
            if  expiration_time < datetime.now().astimezone():
                raise HTTPException(
                    status_code=401,
                    detail="Invalid token or expired token. (exp)")
            if result["token_type"] != "access":
                raise HTTPException(
                    status_code=401, 
                    detail="Invalid token or expired token. (token_type)")

        except Exception as e:
            raise HTTPException(
                status_code=401,
                detail=f"Invalid token or expired token.{e}")

        user_obj = db.query(UserModel).filter(
            UserModel.id == result["user_id"]).one_or_none()
        if not user_obj:
            raise HTTPException(
                status_code=401,
                detail="User Does not Exists")
        return user_obj
