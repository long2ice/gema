from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware

from gema.api import router
from gema.exceptions import http_exception_handler
from gema.static import SPAStaticFiles

app = FastAPI(title="Gema", description="Convert from json/xml to Pydantic/Go/Rust etc.")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(router, prefix="/api")
app.add_exception_handler(HTTPException, http_exception_handler)
app.mount("/", SPAStaticFiles(directory="static", html=True), name="static")
