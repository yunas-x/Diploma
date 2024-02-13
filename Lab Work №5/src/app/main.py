from typing import Optional

from fastapi import (
    FastAPI,
    Body,
    Depends,
    HTTPException,
    status,
    Response
)

from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
import os

from pydantic_models.Programs import (
    ProgramsRequest,
    Program,
    ProgramsFilter,
    ProgramsResponse,
    programs_from_rows
)

from pydantic_models.FieldsOfStudy import (
    FieldOfStudy,
    fields_from_rows_grouped
)

from pydantic_models.HTTPErrors import HTTPAuthError
from orm.queries.ProgramQueries import select_programs

from orm.queries.FieldsQueries import select_fields

from fastapi.responses import RedirectResponse

api_key = os.environ['API_TOKEN']
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def api_key_auth(key: str = Depends(oauth2_scheme)):
    if key != api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Forbidden"
        )

app = FastAPI(title="BI Curricula", 
              summary="""API для дипломного проекта""",
              description="""АПИ к хранилищу данных
                             Для облегчения поиска 
                             образовательных программ""",
              version="0.1.3"
      )

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/fields_of_study",
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
def fields(response: Response) -> list[FieldOfStudy]:
    fields_rows = select_fields()
    fields_list = fields_from_rows_grouped(fields_rows)
    return fields_list


@app.get("/programs",
         dependencies=[Depends(api_key_auth)],
         summary="Список программ",
         description="""Получает список программ""",
         status_code=status.HTTP_200_OK,
         tags=["programs"],
	 responses={
             status.HTTP_200_OK: {
		   "model": ProgramsResponse,
                   "description": "List of programms"
             },
             status.HTTP_401_UNAUTHORIZED: {
                   "model": HTTPAuthError,
                   "description": "Invalid Token (or not provided)"
             }
         }
)
def programs(response: Response,
             args: ProgramsRequest=Depends(ProgramsRequest)
) -> ProgramsResponse:

    programs_rows = select_programs(offset=args.offset,
                                    limit=args.limit)
    programs_list = programs_from_rows(programs_rows)
    return ProgramsResponse(offset=args.offset,
                            limit=args.limit,
                            programs=programs_list)

@app.post("/programs/filter_by",
         dependencies=[Depends(api_key_auth)],
         summary="Список программ по заданному фильтру",
         description="""Получает список программ по заданным условиям""",
         status_code=status.HTTP_200_OK,
         tags=["programs"],
         responses={
             status.HTTP_200_OK: {
                   "model": ProgramsResponse,
                   "description": "List of programms"
             },
             status.HTTP_401_UNAUTHORIZED: {
                   "model": HTTPAuthError,
                   "description": "Invalid Token (or not provided)"
             }
         }
)
def programs_filtered_by(response: Response,
                         filter: Optional[ProgramsFilter]=None,
                         args: ProgramsRequest=Depends(ProgramsRequest)
) -> ProgramsResponse:

    if not filter:
        filter = ProgramsFilter()
    filter_dict = filter.dict(exclude_none=True)
    programs_rows = select_programs(offset=args.offset,
                                    limit=args.limit,
                                    filter=filter_dict)
    programs_list = programs_from_rows(programs_rows)
    return ProgramsResponse(offset=args.offset,
                            limit=args.limit,
                            programs=programs_list)

