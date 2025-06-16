import logging

from fastapi import FastAPI
from contextlib import asynccontextmanager

from infrastructure.configuration.log_config import LOGGING_CONFIG

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logging.config.dictConfig(LOGGING_CONFIG)
    logger = logging.getLogger(__name__)
    logger.info("🚀 App is starting...")

    yield

    # Shutdown
    logger.warning("🛑 App is shutting down...")

