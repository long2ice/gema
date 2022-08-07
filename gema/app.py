from fastapi import FastAPI, HTTPException

from gema.api import router
from gema.exceptions import http_exception_handler

app = FastAPI(
    title="Gema", description="Convert from json/xml to Pydantic/Go/Rust etc."
)
app.include_router(router)
app.add_exception_handler(HTTPException, http_exception_handler)
