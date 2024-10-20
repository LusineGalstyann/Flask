from typing import Optional

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_async_engine("sqlite+aiosqlite:///employee.db")
new_session = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass

async def create_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def delete_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
