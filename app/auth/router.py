from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv

router = InferringRouter(tags=["auth"])

@cbv(router)
class AuthRouter:
    @router.post("/login")
    def login(self):
        return "Login"
        user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

        if not user:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail='Invalid Credentials')
        
        if not utils.verify(user_credentials.password,user.password):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail='Invalid Credentials')
        
        access_token = oauth2.create_access_token(data={'email':user.email,'username':user.username})
        return {'access_token':access_token,'token_type':'bearer'}