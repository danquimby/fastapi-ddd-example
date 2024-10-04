from contextlib import asynccontextmanager
from typing import Iterator, Optional

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    AsyncEngine,
    create_async_engine,
    async_sessionmaker,
)

from app.dependencies import get_settings

engine: AsyncEngine = create_async_engine(
    get_settings().db_url,
    echo=True,
    pool_pre_ping=True,
    pool_size=2,
    max_overflow=0,
    connect_args={
        "timeout": 10,
        "server_settings": {"jit": "off"},
    },
)

async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


@asynccontextmanager
async def get_async_session(
    custom_async_session: Optional[async_sessionmaker] = None,
) -> Iterator[AsyncSession]:
    custom_async_session = custom_async_session or async_session
    async with custom_async_session() as session:
        try:
            yield session
        except SQLAlchemyError:
            await session.rollback()
            raise
        finally:
            await session.close()
