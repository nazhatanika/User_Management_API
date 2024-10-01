# Import necessary types from SQLAlchemy
from sqlalchemy import Column, Integer, String
# Import declarative_base for model definition
from sqlalchemy.ext.declarative import declarative_base

# Create a base class for declarative models
Base = declarative_base()

# Define the User model class, which will represent the 'users' table in the database
class User(Base):
    # Specify the name of the database table
    __tablename__ = 'users'

    # Define the columns of the 'users' table
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    age = Column(Integer)
