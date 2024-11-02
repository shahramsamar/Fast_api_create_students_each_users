from sqlalchemy import Column, Integer, String, ForeignKey
from database.database import Base
from sqlalchemy.orm import relationship

class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer,
                primary_key=True,
                autoincrement=True)
    username = Column(String,
                      unique=True)
    password = Column(String)
    tokens = relationship("TokenModel", 
                          back_populates="user")
    
   # One-to-Many relationship with StudentModel
    students = relationship("StudentModel", back_populates="user", cascade="all, delete-orphan")

    
    def __str__(self):
        return f"{self.id} - {self.username}"
