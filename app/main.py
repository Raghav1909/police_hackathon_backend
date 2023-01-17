from fastapi import FastAPI
from auth import router as auth_router
from users import router as users_router
from database import engine
import models

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(auth_router.router)
app.include_router(users_router.router)

@app.get("/")
def read_root():
    return "Police Hackathon 2023"


