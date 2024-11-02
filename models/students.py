from sqlalchemy import Column, Integer, String,ForeignKey
from database.database import Base
from sqlalchemy.orm import relationship

class StudentModel(Base):
    __tablename__ = "students"

    id = Column(Integer,
                primary_key=True, 
                autoincrement=True)
    name = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    
   
    # ForeignKey linking each student to a specific user
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Many-to-One relationship with UserModel
    user = relationship("UserModel", back_populates="students")

    def __str__(self):
        return f"{self.id} - {self.name} - User ID: {self.user_id}"