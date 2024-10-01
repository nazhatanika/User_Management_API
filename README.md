# User Management API

This is a simple FastAPI application for managing user profiles.
Features include: 
- Create, read, list, update, and delete user profiles.
- Input validation using Pydantic.
- SQLite for data storage.

## Steps For Installation

1. Clone the repository.
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment: 
   - On macOS/Linux: `source venv/bin/activate`
   - On Windows: `venv\Scripts\activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run the application: `uvicorn main:app --reload`

## API Endpoints and Their Functions
- `POST /users/` - Create a new user
- `GET /users/{user_id}` - Get a user by ID
- `PUT /users/{user_id}` - Update a user
- `DELETE /users/{user_id}` - Delete a user
- `GET /users/` - List all users# User_Management_API
