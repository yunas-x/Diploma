from typing import Annotated
import uvicorn

from fastapi import FastAPI, HTTPException, Header, Response, status
from fastapi.responses import RedirectResponse

from .api.models.Program import ProgramsResponse, get_programs

from .api.models.Reports import (
    DeleteReportRequest,
    DeleteResponse,
    ReportRequest, 
    ReportsResponse,
    UpdateResponse,
    add_report,
    check_report, 
    delete_report_by_id, 
    get_reports_by_userid, 
    update_report_by_id
)

from .api.models.User import (
    User,
    UserLogin,
    UserRequest,
    UserResponse,
    UserTokenResponse, 
    add_user, 
    login, 
    find_user, 
    get_id_by_username,
    validate
)


app = FastAPI(title="BI Curricula", 
              summary="""АПИ для дипломного проекта,
                         Разработан модуль для подачи сообщений 
                         об ошибках от пользователей""",
              description="""АПИ к хранилищу данных
                             Для облегчения поиска 
                             образовательных программ""",
              version="0.1.3")

@app.post("/users/create", 
          summary="Создать пользователя",
          description="""Создает тестового пользователя
                         с заданным именем и паролем""",
          status_code=status.HTTP_201_CREATED,
          tags=["users"])
async def users_create(request: UserRequest,
                       response: Response) -> UserResponse:
    
    user = find_user(request)
    if user.success:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return user
    
    user_response = add_user(request)
    if not user_response.success:
        response.status_code = status.HTTP_400_BAD_REQUEST

    return user_response
    
@app.post("/users/login",
          summary="Войти в систему",
          description="""Выполняет вход в систему при правильном вводе логина и пароля""",
          status_code=status.HTTP_200_OK,
          tags=["users"])
async def users_login(request: UserLogin,
                      response: Response) -> UserTokenResponse:
    
    user = find_user(request)
    if not user.success:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return user
    
    user_response = login(request)
    if not user_response.success:
        response.status_code = status.HTTP_400_BAD_REQUEST
    
    return user_response

@app.get("/users/{username}/reports",
          summary="Вернуть обращения в поддержку",
          description="""Возвращает обращения в поддержку для выбранного пользователя""",
          response_class = RedirectResponse,
          status_code=status.HTTP_302_FOUND,
          tags=["users"])
async def get_users_reports(username: str, 
                            xxx_token: Annotated[int, Header()]):
    return RedirectResponse(url=f"/reports/{username}",
                            headers={"xxx_token": xxx_token})

@app.get("/reports/{username}",
          summary="Вернуть обращения в поддержку",
          description="""Возвращает обращения в поддержку для выбранного пользователя""",
          status_code=status.HTTP_200_OK,
          tags=["reports"])
async def get_reports_by_user_id(username: str,
                                 xxx_token: Annotated[int, Header()],
                                 response: Response) -> ReportsResponse:
    id = get_id_by_username(User(username=username))
    if not validate(id=id[0], token=xxx_token):
        response.status_code = status.HTTP_401_UNAUTHORIZED
        raise HTTPException(401, "Invalid token")
    reports = get_reports_by_userid(id[0])
    if id is None:
        response.status_code = status.HTTP_404_NOT_FOUND
    return reports
    

@app.post("/reports",
          summary="Отправить обращение в поддержку",
          description="""Отправляет обращение в поддержку""",
          status_code=status.HTTP_201_CREATED,
          tags=["reports"])
async def send_report(report: ReportRequest, 
                      xxx_token: Annotated[int, Header()],
                      response: Response) -> UpdateResponse:
    
    if not validate(id=report.user_id, token=xxx_token):
        response.status_code = status.HTTP_401_UNAUTHORIZED
        raise HTTPException(401, "Invalid token")
    post_report = add_report(report)
    if not post_report.status:
        response.status_code = status.HTTP_400_BAD_REQUEST
    return post_report
    

@app.put("/reports/{report_id}",
         summary="Изменить обращение в поддержку",
         description="""Изменить выбранное обращение в поддержку""",
         status_code=status.HTTP_202_ACCEPTED,
         tags=["reports"])
async def modify_report(report_id: int,
                        report: ReportRequest,
                        xxx_token: Annotated[int, Header()],
                        response: Response) -> UpdateResponse:
    
    if not validate(id=report.user_id, token=xxx_token):
        response.status_code = status.HTTP_401_UNAUTHORIZED
        raise HTTPException(401, "Invalid token")
    if not check_report(id=report_id, user_id=report.user_id):
        response.status_code = status.HTTP_403_FORBIDDEN
        raise HTTPException(403, "Cannot Modify this")
    upd_report = update_report_by_id(report_id, report.text)
    if not upd_report.status:
        response.status_code = status.HTTP_400_BAD_REQUEST
    return upd_report

@app.delete("/reports/{report_id}",
            summary="Удалить обращение в поддержку",
            description="""Удалить выбранное обращение в поддержку""",
            status_code=status.HTTP_200_OK,
            tags=["reports"])
async def delete_report(report_id: int, 
                        xxx_token: Annotated[int, Header()],
                        xxx_userdata: Annotated[int, Header()], 
                        response: Response) -> DeleteResponse:
    
    if not validate(id=xxx_userdata, token=xxx_token):
        response.status_code = status.HTTP_401_UNAUTHORIZED
        raise HTTPException(401, "Invalid token")
    if not check_report(id=report_id, user_id=xxx_userdata):
        response.status_code = status.HTTP_403_FORBIDDEN
        raise HTTPException(403, "Cannot Modify this")
    _status = delete_report_by_id(report_id)
    if not _status.status:
        response.status_code = status.HTTP_400_BAD_REQUEST
    return _status
    

@app.get("/programs",
         summary="Список программ",
         description="""Получает список программ""",
         status_code=status.HTTP_200_OK,
         tags=["programs"])
async def get_program_on(offset: int|None, response: Response) -> ProgramsResponse:
    if offset is None:
        offset = 0
    return get_programs(offset)

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="127.0.0.1", 
        port=8080, 
        log_level="debug", 
    )