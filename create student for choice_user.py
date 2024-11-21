from database.database import SessionLocal
from models.user import UserModel
from models.students import StudentModel


# Create a database session
db = SessionLocal()

try:
    # Fetch all students and display their details
    users = db.query(UserModel).all()
    for stu in users:
        print(f"ID: {stu.id}, Name: {stu.username}")

    # Ask the user for the student ID
    num = int(input("Enter the ID of the users you want to create a post for: "))

    # Find the student with the matching ID
    selected_users = db.query(UserModel).filter(UserModel.id == num).first()

    if selected_users:
    # Logic for creating a post (example placeholder)
        print(f"Creating a post for User ID {selected_users.id}, Username: {selected_users.username}")
    
        # Create a new student for the selected user
        student = StudentModel(
            name=f"Student for User - {selected_users.username}",
            first_name=f"Student for User - {selected_users.username}",
            # last_name=f"Stud9ent for User {selected_users.last_name}",
            user_id=selected_users.id  # Assuming `StudentModel` has a foreign key `user_id`
        )
        db.add(student)  # Add the new student to the database session
        db.commit()  # Commit the transaction to save changes
        
        print(f"Student created successfully with ID {student.id} and Name {student.name}")
    else:
        print("User not found.")

finally:
    # Close the session
    db.close()