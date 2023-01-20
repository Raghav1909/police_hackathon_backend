from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from fastapi import Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from auth import utils, oauth2
from database import get_db
import models

router = InferringRouter(tags=["auth"])

@cbv(router)
class AuthRouter:
    db: Session = Depends(get_db)

    @router.post("/auth")
    def login(self, user_credentials: OAuth2PasswordRequestForm = Depends()):
        user = self.db.query(models.User).filter(models.User.email == user_credentials.username).first()

        if not user:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail='Invalid Credentials')
        
        if not utils.verify(user_credentials.password,user.password):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail='Invalid Credentials')
        
        access_token = oauth2.create_access_token(data={'email':user.email,'username':user.username})
        return {'access_token':access_token,'token_type':'bearer'}