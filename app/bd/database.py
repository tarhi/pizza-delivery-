from typing import Callable

from fastapi import FastAPI
from sqlalchemy import orm
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    create_async_engine,
    AsyncSession
)



Base = declarative_base()                                    # declaration d'une base de données

class Database:
    def __init__(self, db_url) -> None:
        print(f"db_url {db_url}")
        
        
        self._engine : AsyncEngine = create_async_engine(
            url=db_url,
            echo= False,
            connect_args= {"cheek_same_threed" :True}      # La non partage des donnée, partage des donnee pour eviter la corruption des données on mets "cheek_same_threed" :True
            
            )                                                  #creattion d'un moteur de connexion
# on va créer les sessions avec parametre comme autocommit... et liée la session au engine        
        self._session_factory= orm.scoped_session(
            class_ = AsyncSession,
            autocommit= False,
            autoflush= False,
            bind = self._engine
        )
        
#  on va creer une base de donnee qui va rien retourner

async def create_database(self) -> None:
    async with self._engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
aysc_session = sessionmaker(AsyncEngine)

async def get_session():
    session = aysc_session()
    try:
        yield session
    except  Exception as err:
        print(f"session rollback because of exception : {err}")
        await session.rollback()
        raise ("error")
    finally:
        session.close()
        
    

    
    
        
        
        
        
        
        