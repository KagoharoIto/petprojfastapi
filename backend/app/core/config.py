"""App configuration functions and access to settings"""
from fastapi import FastAPI
from backend.app.core.settings import AppSettings


def get_app_settings() -> AppSettings:
    return AppSettings()


def add_middleware(app: FastAPI) -> None:
    """Function to implement middleware.

    Not implemented yet.
    """
    pass