import os
import ssl
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

raw_url = os.getenv("DATABASE_URL", "postgresql+asyncpg://myuser:mypassword@localhost:5432/mydb")

DATABASE_URL = raw_url.split("?", 1)[0]

ssl_ctx = ssl.create_default_context()

engine = create_async_engine(DATABASE_URL, echo=True, connect_args={"ssl": ssl_ctx})

AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()

# Dependency for async sessions
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
