# Import the create_engine function to manage database connections
from sqlalchemy import create_engine
# Import sessionmaker to create session classes for database interaction
from sqlalchemy.orm import sessionmaker

# Define the database URL for SQLite
DATABASE_URL = "sqlite:///./users.db"

# Create a new SQLAlchemy engine instance using the DATABASE_URL
# The engine will handle the connection to the SQLite database
engine = create_engine(DATABASE_URL)

# Create a new session class (SessionLocal) that will be used to interact with the database
# autocommit=False means changes must be explicitly committed
# autoflush=False means changes are not automatically flushed to the database before queries
# bind=engine connects this session to the previously created engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)