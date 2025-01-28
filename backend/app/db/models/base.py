"""Declaring base model classes for sqlalchemy models."""
from sqlalchemy import Column, Integer
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncAttrs, create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import mapped_column, declarative_base, declarative_mixin, Mapped, DeclarativeBase
from sqlalchemy.sql import func
from backend.app.core.config import get_app_settings
from backend.app.db.models.metadata import metadata_family


Base = declarative_base()

settings = get_app_settings()
engine = create_async_engine(url=settings.database_url)
async_session_maker = async_sessionmaker(engine, class_=AsyncSession)


@declarative_mixin
class BaseDBModel(AsyncAttrs, DeclarativeBase):
    """Class defining common db model components."""
    __metadata__ = metadata_family
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())
    __name__: str

    # if not declared generate tablename automatically based on class name
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    # refresh server defaults with asyncio
    # https://docs.sqlalchemy.org/en/14/orm/extensions/asyncio.html#synopsis-orm
    # required in order to access columns with server defaults
    # or SQL expression defaults, subsequent to a flush, without
    # triggering an expired load
    __mapper_args__ = {"eager_defaults": True}
