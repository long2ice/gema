from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from gema.api import router

app = FastAPI(title="Gema", description="Convert from json/xml to Pydantic/Go/Rust etc.")
app.include_router(router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)
