from database.database import SessionLocal
from models.user import UserModel


# create a new database session
session = SessionLocal()

try:
    print("give me username and password for create user :")
    username = input("Enter username :").lower()
    password = input("Enter password :").lower()
    
    # create a user
    create_user = UserModel(username=username, password=password)
    
    # add the user to the session
    session.add(create_user)
    
    # commit the transaction
    session.commit()
    print("Create User Added Successfully")

except Exception as e :
    # Rollback the transaction in case of KeyError
    session.rollback()
    print("Error adding create user :{e}")



finally:
    # close the session 
    session.close()        
    
    
    
