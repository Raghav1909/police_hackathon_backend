from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from auth import router as auth_router
from users import router as users_router
from data_analytics import router as data_router
from database import engine
import models

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router.router)
app.include_router(users_router.router)
app.include_router(data_router.router)

@app.get("/")
def read_root():
    return "Police Hackathon 2023"


