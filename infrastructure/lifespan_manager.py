import logging
from fastapi import FastAPI
from contextlib import asynccontextmanager
from tenacity import retry, wait_fixed, stop_after_attempt
from sqlalchemy import text

from infrastructure.configuration.db_config import test_db_connection, get_async_db
from infrastructure.configuration.log_config import LOGGING_CONFIG

@retry(wait=wait_fixed(2), stop=stop_after_attempt(5), reraise=True)
async def ensure_connection(service):
    logging.info("🔁 Trying to connect to the database...")
    await service()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logging.config.dictConfig(LOGGING_CONFIG)
    logger = logging.getLogger(__name__)
    logger.info("🚀 App is starting...")

    #db connection
    try:
        await ensure_connection(test_db_connection)
        logging.info("--------------- Connected to PostgreSQL -----------------")
    except Exception as e:
        logging.error(f"Failed to connect to PostgreSQL: {e}")
        raise e

    try:
        yield

    finally:
        logger.warning("🛑 App is shutting down...")
        logging.info("----------- Disconnected from PostgreSQL -----------")
