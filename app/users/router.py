from fastapi import APIRouter, Depends, Response, status, HTTPException
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from auth.oauth2 import get_current_user
from auth import utils
from users import schemas
import models
from database import get_db
from sqlalchemy.orm import Session

router = InferringRouter(tags=["users"])

@cbv(router)
class UserRouter:
    #current_user: int = Depends(get_current_user)
    db: Session = Depends(get_db)

    @router.get("/users")
    def get_users(self) -> list[schemas.UserBase]:
        db_user = self.db.query(models.User).all()
        return db_user
    
    @router.get("/users/{username}")
    def get_user(self, username: str) -> schemas.UserBase:
        db_user = self.db.query(models.User).filter(models.User.username == username).first()
        return db_user
    
    @router.post("/users")
    def create_user(self, user: schemas.UserCreate):
        if self.db.query(models.User).filter(models.User.username == user.username).first():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail='Username already exists')
        
        if self.db.query(models.User).filter(models.User.email == user.email).first():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f'User with email {user.email} already exists')
        user.password = utils.hash(user.password)
        new_user = models.User(**user.dict())
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return Response(status_code=status.HTTP_201_CREATED)
