# base view model 

from typing import Optional

from starlette.requests import Request

from app.core.cookies.cookie_auth import get_user_id_via_cookie


class ViewModelBase:
    
    def __init__(self,request:Request) -> None:
        self.request:Request = request
        self.error: Optional[str] = None
        self.user_id :Optional[int] = get_user_id_via_cookie(self.request)
        
    def to_dict(self) -> dict:
        return self.__dict__