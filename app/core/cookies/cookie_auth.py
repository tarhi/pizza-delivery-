# cookie authentification models

from typing import Optional
import hashlib
from fastapi import (
    Request,
    Response
)
from app.core.viewmodels import config 

auth_cookie_name = config.AUTH_COOKIE_NAME


# quand mon utilisateur se connecte sur mon systeme, je vais créer un cookie

def set_auth(response:Response, user_id:int)-> None:
    hash_user_id = __hash_text(str(user_id))
    val= f"{user_id}:{hash_user_id}"
    response.set_cookie(auth_cookie_name,val, secure=False, httponly=True, samesite="Lax")
    
    
    
def __hash_text(text:str):
    text = "_salty"+text+"__text"
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


# recupération de user id a travers les cookies 
# request pour récupérer des données d'une page web 

def get_user_id_via_cookie(request:Request)-> Optional[int]:
    if auth_cookie_name not in request.cookies:
        return None
    val = request.cookies[auth_cookie_name]
    
    part= val.split()
    
    if len(part) !=2:
        return None
    user_id = part[0]
    hash_user_id = part[1]
    
    hash_user_id_cheek = __hash_text(user_id)
    
    if hash_user_id_cheek != hash_user_id:
        print("invalid cookies")
        return None
