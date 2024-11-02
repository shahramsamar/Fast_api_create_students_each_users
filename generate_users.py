from database.database import SessionLocal
from models.user import UserModel
from models.students import StudentModel
from faker import Faker

fake = Faker()
session = SessionLocal()

try:
    # Step 1: Create 5 users
    users = []
    for _ in range(5):
        user = UserModel(
            username=fake.unique.user_name(),
            password=fake.password()
        )
        session.add(user)
        users.append(user)

    # Commit to save users and get their IDs
    session.commit()

    # Step 2: For each user, create 5 students linked to that user
    for user in users:
        for _ in range(5):
            student = StudentModel(
                name=fake.name(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                user_id=user.id
            )
            session.add(student)
        print(f"Created _ students for user: {user}")

    # Commit all students
    session.commit()

except Exception as e:
    session.rollback()
    print(f"Error: {e}")

finally:
    session.close()
