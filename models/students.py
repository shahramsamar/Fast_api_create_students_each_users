from sqlalchemy import Column, Integer, String,Boolean,DateTime
from database.database import Base


class StudentModel(Base):
    __tablename__ = "students"

    id = Column(Integer,
                primary_key=True, 
                autoincrement=True)
    name = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    
    def __str__(self):
        return f"{self.id } - {self.name}"
