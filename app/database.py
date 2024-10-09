from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, sessionmaker
from sqlalchemy.orm import declarative_base
import os

# Get the database connection URL
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://username:password@localhost/dbname")

# Create an asynchronous engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Asynchronous session
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# Base for the models
Base = declarative_base()

# Function to get a database session
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

# Function to create all tables in the database
async def create_all():
    async with engine.begin() as conn:
        # Create all tables based on the models
        await conn.run_sync(Base.metadata.create_all)
