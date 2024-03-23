# repositories auth module

# lobjectif est de comparer le mot de passe hash et le mot de passe en text clair pour pouvoir se Connecter 
# cest a dire on va crée le busines logique de la fonctionalité authentification 

import logging
from contextlib import AbstractAsyncContextManager
from typing import Callable, Optional

from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2AuthorizationCodeBearer
from sqlalchemy.future import select

from app.user.schemas import (
    UserLogin,
    UserCreate
)

from app.user.models import User


pwd_context = CryptContext(schemes=["Bcrypt"], deprecated="auto")


# ce constructeur va nous permettre de se comminiquer avec notre base de donnée pour pour faire des requettes 

class AuthRepositories:
    def __init__(self, session_factory: Callable[..., AbstractAsyncContextManager[AsyncSession]]) -> None:
        self.session_factory = session_factory
# user va nous communiquer un mot de passe en text claire qui sera stocker dans la base de donnée, par la suite on va 
# hashe ce mot de passe  a travers la methode pwd_context

def get_password_hash(self, password:str)->str:
    return pwd_context.hash(password)

def verify_password_hash(self, plain_password:str, hashed_password:str) -> bool:
    return pwd_context.verify(plain_password,hashed_password)


async def get_user_by_email(self, email: str) -> Optional[User]:
    async with self.session_factory() as session:
        query = select(User).filter(User.email== email)
        result = await session.execute(query)
        user= result.scalar_one_or_none()
    
    if user is None:
            return None
    return user

async def login_user(self, user_login: UserLogin) ->Optional[User]:
    user = await self.get_user_by_email(user_login.email)
    if  not get_user_by_email(user_login.email):
        None
    if verify_password_hash(user_login.password):
        None
    return user
        
        
        
        
        
        
        
        
        
        
    
    # if user is None:
    #     return None
    # if not self.verify_password_hash(user_login.password, User.hash_password):
    #     return None
    # return user


        









