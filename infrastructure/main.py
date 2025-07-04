import os
import logging

from fastapi import FastAPI, Path, Query
import uvicorn
from dotenv import load_dotenv

from infrastructure.lifespan_manager import lifespan

from infrastructure.routes.api_router import router

load_dotenv()

app = FastAPI(
    lifespan=lifespan,
    descriptionl="Discord-mgt-service-for-PGL",
    debug=True
)

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app.include_router(router)

if __name__== "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        workers=1)
