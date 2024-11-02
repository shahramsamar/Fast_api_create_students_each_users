from audioop import add
from database.database import SessionLocal
from models.students import StudentModel
from faker import Faker

fake = Faker()

# fake = Faker("fa_IR")

# create a new database session
session = SessionLocal()

try:
    # generate a list of sample students
    students = [StudentModel(name=fake.name(),
                            first_name=fake.first_name(),
                            last_name=fake.last_name())
                            for _ in range(5)]
    
    
    # add all the sample  students ti the session in bulk
    session.bulk_save_objects(students)
    
    # # create a sample student
    # sample_Student = StudentModel(name=fake.name(), first_name=fake.first_name(),last_name = fake.last_name())
    
    # # add the user to the session
    # session.add(sample_Student)
    
    
    
    # commit the transaction
    session.commit()
    print("Create Student Added Successfully")

except Exception as e :
    # Rollback the transaction in case of KeyError
    session.rollback()
    print("Error adding create student :{e}")



finally:
    # close the session 
    session.close()        
    
    
    
