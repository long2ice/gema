from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.status import HTTP_404_NOT_FOUND
from starlette.templating import Jinja2Templates
from fastapi.exception_handlers import http_exception_handler as exception_handler
from starlette.exceptions import HTTPException as StarletteHTTPException
from gema.api import router
from gema.exceptions import http_exception_handler

app = FastAPI(
    title="Gema", description="Convert from json/xml to Pydantic/Go/Rust etc."
)
app.include_router(router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)
app.add_exception_handler(HTTPException, http_exception_handler)

app.mount("/", StaticFiles(directory="static", html=True), name="static")
templates = Jinja2Templates(directory="static")


@app.exception_handler(StarletteHTTPException)
async def spa_server(request: Request, exc: StarletteHTTPException):
    if exc.status_code == HTTP_404_NOT_FOUND:
        return templates.TemplateResponse("index.html", context={"request": request})
    else:
        return await exception_handler(request, exc)
