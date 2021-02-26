
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from .config import settings, Settings
from .models import create_models
from .api import router
from .logging import simple_logging


create_models()

app = FastAPI(title=f'API - {settings.app_name}')
app.include_router(router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_allowed_origins,
    allow_methods=settings.cors_allowed_methods,
    allow_headers=settings.cors_allowed_headers,
)


@app.middleware("http")
async def logging(request: Request, call_next):
    response = await call_next(request)
    await simple_logging(request, response)
    return response


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
