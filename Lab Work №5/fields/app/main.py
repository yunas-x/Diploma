from fastapi import (
    FastAPI,
    Depends,
    HTTPException,
    status,
    Response,
    Header
)

from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from custom_requests import auth, try_get_fields

from pydantic_models.FieldsOfStudy import (
    FieldOfStudy,
    fields_from_rows_grouped
)

from typing import Annotated
from pydantic_models.HTTPErrors import HTTPAuthError

from orm.queries.Queries import select_fields

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def api_key_auth(key: str = Depends(oauth2_scheme)):
    if auth(key):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Forbidden"
        )

app = FastAPI(title="BI Curricula", 
              summary="""API для дипломного проекта""",
              description="""АПИ к хранилищу данных
                             Для облегчения поиска 
                             образовательных программ""",
              version="0.1.3",
              root_path="/fields"
      )

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/",
         dependencies=[Depends(api_key_auth)],
         summary="Список направлений подготовки",
         description="""Получает направлений подготовки""",
         status_code=status.HTTP_200_OK,
         tags=["fields of study"],
         responses={
             status.HTTP_200_OK: {
                   "model": list[FieldOfStudy],
                   "description": "List of fields of study"
             },
             status.HTTP_401_UNAUTHORIZED: {
                   "model": HTTPAuthError,
                   "description": "Invalid Token (or not provided)"
             }
         }
)
def fields(response: Response, authorization: Annotated[str | None, Header()] = None) -> list[FieldOfStudy]:
    
    fields_codes_filter = [f['field_code']
                           for f in try_get_fields(authorization).json()["field_codes"]]
    fields_rows = select_fields(fields_codes_filter)
    fields_list = fields_from_rows_grouped(fields_rows)
    return fields_list
