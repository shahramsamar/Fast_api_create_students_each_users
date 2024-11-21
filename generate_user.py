from database.database import SessionLocal
from models.user import UserModel
from faker import Faker

fake = Faker()

# create a new database session
session = SessionLocal()

try:
    # print("give me username and password for create user :")
    # generate a list of sample students
    # user = [UserModel(
    #                         username=fake.user_name(),
    #                         password=fake.password())
    #                         for _ in range(5)]
    # add all the sample  students ti the session in bulk
    # session.bulk_save_objects(user)
    
    for _ in range(1):
        print("Give me a username and password to create a user:")
        username = input("Enter username: ").lower()
        password = input("Enter password: ").lower()

        # Create a user instance
        user = UserModel(username=username, password=password)

        # Add the user to the session
        session.add(user)

        # Commit the transaction
        session.commit()
        print("User created successfully.")

except Exception as e:
    # Rollback the transaction in case of an error
    session.rollback()
    print(f"Error adding user: {e}")

finally:
    # Close the session
    session.close()
    
    
