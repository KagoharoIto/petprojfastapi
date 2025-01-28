from fastapi import FastAPI
from loguru import logger

from backend.app.api.routes.router import router as api_router
from backend.app.core.config import add_middleware, get_app_settings
from backend.app.db.db_session import initialize_database


def get_app() -> FastAPI:
    """Instanciating and setting up FastAPI application."""
    settings = get_app_settings()

    app = FastAPI(**settings.fastapi_kwargs)

    add_middleware(app)

    app.include_router(api_router, prefix=settings.api_prefix)

    @app.on_event("startup")
    async def startup_event() -> None:
        await initialize_database()

    settings.configure_logging()

    return app


app = get_app()


@app.get("/")
async def root():

    return {"message": "OK"}


@app.get("/settings")
async def get_app_info():
    settings = get_app_settings()
    info = {
        "app_env": settings.app_env,
        "db_settings": settings.database_settings,
        "database url": settings.database_url,
        "app info": settings.fastapi_kwargs,
    }

    return info


@app.get("/logger_test")
async def test_logger():
    logger.info("This is an info")
    logger.warning("This is a warning")
    logger.error("This is an error")
    logger.critical("Shit's about to blow up")

    return {"message": "See log types produced by app"}