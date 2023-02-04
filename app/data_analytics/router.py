from fastapi import Depends, Response, status, HTTPException, File, UploadFile
from fastapi_utils.inferring_router import InferringRouter
from fastapi.responses import JSONResponse
from fastapi_utils.cbv import cbv
from database import get_db, engine
from sqlalchemy.orm import Session
import models
from tempfile import NamedTemporaryFile
from datetime import date
from data_analytics import schemas
import pandas as pd

router = InferringRouter(tags=["data"])

@cbv(router)
class DataRouter:
    #current_user: int = Depends(get_current_user)
    db: Session = Depends(get_db)
    @router.post("/data")
    def convert_data_from_csv(self, csv_file: UploadFile = File(...)):
        df = pd.read_csv(csv_file.file)
        df.to_sql('police_database', con=self.db.bind, if_exists='append', index=False)
        return Response(status_code=status.HTTP_201_CREATED)
    
    @router.get("/data/search")
    def search(q: str):
        try:
            # Read the table into a pandas DataFrame
            df = pd.read_sql_table("table", con=engine)

            # Search all columns for the query string
            result = df.where(pd.Series([i for i in df.apply(lambda x: x.astype(str).str.contains(q, case=False).any())]))
            result.dropna(how="all", axis=0, inplace=True)

            return JSONResponse(content=result.to_json(orient="records"))
        finally:
            session.close()