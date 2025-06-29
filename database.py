import os
import ssl
from urllib.parse import urlparse
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

raw_url = os.getenv("DATABASE_URL", "postgresql+asyncpg://myuser:mypassword@localhost:5432/mydb")
DATABASE_URL = raw_url.split("?", 1)[0]

# Parse the DB URL to extract the hostname
parsed_url = urlparse(DATABASE_URL)
hostname = parsed_url.hostname

# Disable SSL for localhost or Docker Compose service name "db"
if hostname in ("localhost", "127.0.0.1", "db"):
    connect_args = {}
else:
    ssl_ctx = ssl.create_default_context()
    connect_args = {"ssl": ssl_ctx}

engine = create_async_engine(DATABASE_URL, echo=True, connect_args=connect_args)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()

# Dependency for async sessions
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session