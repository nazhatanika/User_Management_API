# Import BaseModel from Pydantic
from pydantic import BaseModel, EmailStr

# Define a schema for user creation
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: int

# Define a schema for user response
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: int

    # Enable ORM mode to read data from SQLAlchemy models
    class Config:
        orm_mode = True
