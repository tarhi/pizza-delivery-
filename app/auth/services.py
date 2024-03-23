# service auth module 

from typing import Optional

from app.user.models import User
from .repositories import AuthRepositories
from app.user.schemas import(
    UserLogin
)

class AuthServices:
    def __init__(self, auth_repository: AuthRepositories) -> None:
        self.auth_repository: AuthRepositories = auth_repository
        
        async def login_user(self, user_login: UserLogin) ->Optional[User]:
            user = await self.repository.login_user(user_login)