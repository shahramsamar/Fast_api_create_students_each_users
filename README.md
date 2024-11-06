# FastAPI Create Students for Each User

A FastAPI project that allows users to create and manage student records, with each user having their own set of students. This application uses FastAPI for the web framework and SQLAlchemy for ORM-based database interaction.

## Features

- **User Registration**: Allows users to register with their details (username and password).
- **Student Management**: Users can create, read, update, and delete students within their own accounts.
- **Data Validation**: Ensures that data for both users and students are validated using Pydantic models.
- **Authentication**: Users must authenticate using JWT tokens to perform operations related to students.
- **Role-Based Access**: Each user can manage their own students but cannot access other users' data.

## Requirements

- **Python 3.x**
- **FastAPI**: Web framework for building APIs.
- **Uvicorn**: ASGI server for serving the FastAPI app.
- **SQLAlchemy**: ORM for interacting with the database.
- **Pydantic**: Data validation library.
- **SQLite**: The default database used for this project.
- **JWT (JSON Web Tokens)**: Used for user authentication.

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/shahramsamar/Fast_api_create_students_each_users.git
    cd Fast_api_create_students_each_users
    ```

2. **Install Dependencies:**

    If you're using `pip`, run:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application:**

    To run the FastAPI app using Uvicorn:

    ```bash
    uvicorn main:app --reload
    ```

    This will start the server at `http://127.0.0.1:8000`.

### How to Use

1. **Register a User**:
    - Send a `POST` request to `/register/` with the username and password to create a new user.

    Example request body:
    ```json
    {
        "username": "user1",
        "password": "securepassword"
    }
    ```

2. **Login and Get Token**:
    - Send a `POST` request to `/login/` with the username and password to receive a JWT token.

    Example request body:
    ```json
    {
        "username": "user1",
        "password": "securepassword"
    }
    ```

    Response will include the JWT token to be used in subsequent requests.

3. **Create a Student**:
    - Send a `POST` request to `/students/` with student data, and include the JWT token in the authorization header.

    Example request body:
    ```json
    {
        "name": "John Doe",
        "age": 20,
        "major": "Computer Science"
    }
    ```

4. **Get All Students**:
    - Send a `GET` request to `/students/` to retrieve all students associated with the authenticated user.

5. **Update a Student**:
    - Send a `PUT` request to `/students/{student_id}/` to update student details.

6. **Delete a Student**:
    - Send a `DELETE` request to `/students/{student_id}/` to remove a student.

### Example Endpoints

- **Register User**: `POST /register/`
- **Login and Get Token**: `POST /login/`
- **Create Student**: `POST /students/`
- **Get All Students**: `GET /students/`
- **Update Student**: `PUT /students/{student_id}/`
- **Delete Student**: `DELETE /students/{student_id}/`

### Project Structure

- `main.py`: Contains the FastAPI application, route handlers, and database setup.
- `models.py`: Defines SQLAlchemy ORM models for User and Student.
- `schemas.py`: Contains Pydantic models for validation and response formatting.
- `auth.py`: Handles authentication logic using JWT.
- `requirements.txt`: Lists necessary libraries and dependencies for the project.

### API Documentation

FastAPI automatically generates interactive API documentation:

- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

### Example Requests

1. **Register User** (POST):
    ```bash
    curl -X 'POST' \
    'http://127.0.0.1:8000/register/' \
    -H 'Content-Type: application/json' \
    -d '{
        "username": "user1",
        "password": "securepassword"
    }'
    ```

2. **Login and Get Token** (POST):
    ```bash
    curl -X 'POST' \
    'http://127.0.0.1:8000/login/' \
    -H 'Content-Type: application/json' \
    -d '{
        "username": "user1",
        "password": "securepassword"
    }'
    ```

3. **Create Student** (POST):
    ```bash
    curl -X 'POST' \
    'http://127.0.0.1:8000/students/' \
    -H 'Authorization: Bearer your_jwt_token' \
    -H 'Content-Type: application/json' \
    -d '{
        "name": "John Doe",
        "age": 20,
        "major": "Computer Science"
    }'
    ```

4. **Get All Students** (GET):
    ```bash
    curl -X 'GET' \
    'http://127.0.0.1:8000/students/' \
    -H 'Authorization: Bearer your_jwt_token'
    ```

### Contributing

Feel free to fork the project and submit pull requests for new features, improvements, or bug fixes.

## License

This project is open-source and available for educational purposes.

