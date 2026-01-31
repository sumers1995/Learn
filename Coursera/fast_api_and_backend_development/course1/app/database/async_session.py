from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from app.database.models import Shipment
from app.database.config import DatabaseSettings

Base = declarative_base()
settings = DatabaseSettings()
engine = create_async_engine(
    url=settings.POSTGRES_URL,
    echo=True,
)

async def create_db_tables():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
        
async def get_session():
    async_session = sessionmaker(bind=engine, class=AsyncSession, expire_on_commit=False,)
    async with async_session() as session:
        yield session


SessionDep = Annotated[AsyncSession, Depends(get_session)]

if __name__ == "__main__":
    session = get_session()
    results = session.get(Shipment, 1033)
    dic = results.model_dump()
    print(dic)