import asyncio
import logging

from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import sessionmaker

from infrastructure.configuration.db_settings import settings

SQL_ALCHEMY_ASYNC_DATABASE_URL = settings.async_database_url

async_engine = create_async_engine(
    SQL_ALCHEMY_ASYNC_DATABASE_URL,
    echo = True,
    future= True,
    pool_pre_ping=True,
    pool_recycle=300,
)

AsyncSessionLocal =sessionmaker(bind=async_engine, class_=AsyncSession, expire_on_commit=False)

async def get_async_db():
    async with AsyncSessionLocal() as db:
        try:
            yield db
        finally:
            await db.close()

        
async def test_db_connection():
    try:
        await asyncio.wait_for(
            _try_query(),
            timeout=10.0  # Increased timeout
        )
        logging.info("✅ Database connection successful!")
    except asyncio.TimeoutError:
        raise RuntimeError("Database connection timed out after 10 seconds.")
    except Exception as e:
        logging.error(f"Database connection failed: {e}")
        raise

async def _try_query():
    async with async_engine.begin() as conn:
        logging.info("Executing test query...")
        result = await conn.execute(text("SELECT 1 as test"))
        row = result.fetchone()
        logging.info(f"Test query result: {row}")
