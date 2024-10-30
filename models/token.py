from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database.database import Base

class TokenModel(Base):
    __tablename__ = "tokens"
    id = Column(Integer, 
                primary_key=True,
                autoincrement=True)
    token = Column(String,
                   unique=True,
                   index=True, 
                   nullable=False)
    expiration_date = Column(DateTime,
                             nullable=False)
    user_id = Column(Integer, 
                     ForeignKey("users.id"))
    user = relationship("UserModel", 
                        back_populates="tokens")