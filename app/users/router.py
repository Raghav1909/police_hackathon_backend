from fastapi import APIRouter, Depends
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from auth.oauth2 import get_current_user


router = InferringRouter(tags=["users"])

@cbv(router)
class UserRouter:
    current_user = Depends(get_current_user)

    @router.get("/users")
    def get_users(self):
        return "These are users"
