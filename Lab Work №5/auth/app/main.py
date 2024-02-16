from fastapi import (
    FastAPI,
    Depends,
    HTTPException,
    status,
    Response
)

from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
import os


from pydantic_models.HTTPErrors import HTTPAuthError
from orm.queries.Queries import add_session, get_session
from pydantic_models.ApiSession import ApiSession

api_key = os.environ['API_TOKEN']
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def api_key_auth(key: str = Depends(oauth2_scheme)):
    if key != api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token (or not provided)"
        )

app = FastAPI(title="BI Curricula", 
              summary="""API для дипломного проекта""",
              description="""АПИ к хранилищу данных
                             Для облегчения поиска 
                             образовательных программ""",
              version="0.1.3",
              root_path="/auth"
      )

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/session",
          dependencies=[Depends(api_key_auth)],
          summary="Получить сессию доступа",
          description="""Получает сессию доступа""",
          status_code=status.HTTP_200_OK,
          tags=["auth"],
	      responses={
              status.HTTP_200_OK: {
		           "model": ApiSession,
                   "description": "Session object"
              },
              status.HTTP_401_UNAUTHORIZED: {
                   "model": HTTPAuthError,
                   "description": "Invalid Token (or not provided)"
              }
         }
)
def create_session(response: Response) -> ApiSession:
    session = add_session()
    return ApiSession(
                      session_id=session.session_id,
                      created_at=session.created_at
                      )    

@app.post("/session/check",
          dependencies=[Depends(api_key_auth)],
          summary="Проверить сессию доступа",
          description="""Проверить сессию доступа""",
          status_code=status.HTTP_200_OK,
          tags=["auth"],
	      responses={
              status.HTTP_200_OK: {
		           "model": ApiSession,
                   "description": "Session object"
              },
              status.HTTP_401_UNAUTHORIZED: {
                   "model": HTTPAuthError,
                   "description": "Invalid Token (or not provided)"
              },
              status.HTTP_403_FORBIDDEN: {
                   "model": HTTPAuthError,
                   "description": "Sessions doesn't exist or expired"
              }
         }
)
def check_session(response: Response, session_id: str) -> ApiSession:
    session = get_session(session_id)
    if not session:
        raise HTTPAuthError(
                            status_code=status.HTTP_403_FORBIDDEN,
                            detail="Sessions doesn't exist or expired"
                           )
    return ApiSession(
                      session_id=session.session_id,
                      created_at=session.created_at
                     )
    
    
