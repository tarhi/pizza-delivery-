from pydantic import BaseModel, Field
from typing import Optional
from typing_extensions import Annotated


class UserBase(BaseModel):
    email: str
    name: Optional[str]=None

class UserOut(BaseModel):
    pass 

class UserLogin(UserBase):
    password : str

class UserCreate(UserBase):
    password : str
    
    class config:
        orm_mode =True
    
# class UserEdit(UserBase):
#     password = str = Field(max_length=10)
    
#     class config:
#         orm_mode =True