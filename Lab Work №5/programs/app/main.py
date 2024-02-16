from typing import Optional

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

from pydantic_models.Programs import (
    ProgramsRequest,
    ProgramsFilter,
    ProgramsResponse,
    programs_from_rows
)

from pydantic_models.Fields import (
    FieldsResponse,
    fields_from_rows
)

from typing import Annotated

from pydantic_models.HTTPErrors import HTTPAuthError
from orm.queries.ProgramQueries import select_programs, select_fields
from custom_requests import auth, get_fields

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

def fields_to_dict(authorization):
    return {f["field_code"]: f 
              for f 
              in get_fields(authorization).json()}

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
             authorization: Annotated[str | None, Header()]=None,
             args: ProgramsRequest=Depends(ProgramsRequest)
) -> ProgramsResponse:

    programs_rows = select_programs(offset=args.offset,
                                    limit=args.limit)
    programs_list = programs_from_rows(programs_rows, 
                                       fields_to_dict(authorization))
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
                         authorization: Annotated[str | None, Header()]=None,
                         filter: Optional[ProgramsFilter]=None,
                         args: ProgramsRequest=Depends(ProgramsRequest)
) -> ProgramsResponse:

    if not filter:
        filter = ProgramsFilter()
    filter_dict = filter.model_dump(exclude_none=True)
    programs_rows = select_programs(offset=args.offset,
                                    limit=args.limit,
                                    filter=filter_dict)
    
    programs_list = programs_from_rows(programs_rows, 
                                       fields_to_dict(authorization))
    return ProgramsResponse(offset=args.offset,
                            limit=args.limit,
                            programs=programs_list)

@app.get("/programs/fields",
         dependencies=[Depends(api_key_auth)],
         summary="Список направлений подготовки",
         description="""Список направлений подготовки, для которых найдены программы""",
         status_code=status.HTTP_200_OK,
         tags=["programs"],
	     responses={
             status.HTTP_200_OK: {
		     "model": FieldsResponse,
                   "description": "List of programms"
             },
             status.HTTP_401_UNAUTHORIZED: {
                   "model": HTTPAuthError,
                   "description": "Invalid Token (or not provided)"
             }
         }
)
def get_field_codes(response: Response) -> FieldsResponse:
    field_codes_rows = select_fields()
    fields = fields_from_rows(field_codes_rows)
    return FieldsResponse(field_codes=fields)
