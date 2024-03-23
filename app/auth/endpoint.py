import asyncio
from typing import Optional

import fastapi.responses
from dependency_injector.wiring import inject, Provide
from fastapi import(
    APIRouter,
    Depends,
    status,
    Request
)

from starlette.responses import RedirectResponse

from app.containers import Containers
from app.core.cookies import cookie_auth
from app.auth.services import AuthServices
from app.core.viewmodels.loginviewmodel import LoginViewModel
from app.user.schemas import(
    UserLogin
)

auth = APIRouter(tags=["Authentification"])

@auth.get("/acount/login")

async def login_get(request:Request):
    user_id = cookie_auth.get_user_id_via_cookie(request)
    if user_id:
        resp = fastapi.responses.RedirectResponse("/", status_code=302)
        return resp
    
    vm = LoginViewModel(request)
    print (f"vm login: {vm}")
    



