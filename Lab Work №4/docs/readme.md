# Разработка BI-системы для исследования учебных планов образовательных программ университетов

API к хранилищу данных для облегчения сравнения образовательных программ и их выбора абитуриентом. Выполняется в рамках комадного проекта и дипломного проекта в НИУ ВШЭ Пермь в рамках обучения на программной инженерии.

## Документация по API
Ниже приведен список планируемых ресурсов и endpoint'ов. Часть из них не реализованы. К реализованным дано краткое пояснение, более подробную информацию, в том числе возвращаемые данные, можно найти в Swagger. Все параметры обязательны, если не указано иное.

### /programs — программы высшего образования
<b> GET </b> /programs — получить все программы высшего образования <br>
<br>
<i> Query parameters: </i> <br>
```- offset ```: положительный integer — номер строки, с которой возвращаются записи из базы данных, по умолчанию равен 0. Можно использовать для пагинации <br>
limit: положительный integer в диапазоне [1..100] — количество возвращаемых записей <br>
<br>
<i> Response: </i> <br>
programs: array[Program] — Список программ высшего образования <br>
Program</b> { <br>
        program_name: string — название программы <br>
        degree_id: integer — уровень обучения <br>
        field_code: string — направление подготовки (Код ОК 009-2016) <br>
        university_id: integer — ID университета <br>}
<br>

### /users — пользователи
<b> POST </b> /users/create — создать пользователя <br>
<i> Body parameters: </i> <br>
username: string (english) — имя пользователя <br>
email: string (email) — E-Mail <br>
password: string (english) — пароль <br>
<br>
<i> Response: </i> <br>
username: string — имя пользователя (не менее 5 символов) <br>
message: string — сообщение об ошибке/успехе <br>
success: boolean — создано/не создано <br>
<br>
<b> POST </b> /users/login — войти в систему <br>
<i> Body parameters: </i> <br>
username: string (english) — имя пользователя <br>
password: string (english) — пароль <br>
<br>
<i> Response: </i> <br>
username: string — имя пользователя (не менее 5 символов) <br>
message: string — сообщение об ошибке/успехе <br>
success: boolean — создано/не создано <br>
token: integer — токен авторизации <br>
<br>
<b> GET </b> /users/{username}/reports — все обращения пользователя <br>
<i> Path parameters: </i> <br>
username: string (english) — имя пользователя <br>
<i> Headers: </i> <br>
xxx-token: integer — токен авторизации <br>
<br>
<i> Redirect on: </i> <b> GET </b> /reports/{username} <br>

### /reports — сообщения об ошибках
Данные запросы завершаются ошибкой при неверных данных пользователя (id или имя пользователя) и токенах авторизации. <br>
При попытке манипуляции с сообщениями проверяется принадлежность токена пользователю. <br>

<b> POST </b> /reports — отправить сообщение об ошибке <br>
<i> Body parameters: </i> <br>
text: string — сообщение об ошибке <br>
user_id: int — id пользователя <br>
<br>
<i> Headers: </i> <br>
xxx-token: integer — токен авторизации <br>
<br>
<i> Response: </i> <br>
text: string — текст сообщения в поддержку <br>
message: string — сообщение об ошибке/успехе <br>
success: boolean — создано/не создано <br>
<br>
<b> GET </b> /reports/{username} — получить все сообщения об ошибке от пользователя <br>
<i> Path parameters: </i> <br>
username: string (english) — имя пользователя <br>
<br>
<i> Headers: </i> <br>
xxx-token: integer — токен авторизации <br>
<br>
<i> Response: </i> <br>
user_id: integer — Id пользователя <br>
message: string — сообщение об ошибке/успехе <br>
success: boolean — получено/не найдено <br>
reports: array[ReportResponse] — cообщения указанного пользователя <br>
<br>
ReportResponse { <br>
text: string — сообщение <br>
id: integer — ID сообщения об ошибке <br>
posted_on: string(date-time) — дата отправки <br>
} <br>
<br>
<b> DELETE </b> /reports/{report_id} — удалить сообщение об ошибке <br>
<i> Path parameters: </i> <br>
report_id: int — id обращения <br>
<br>
<i> Headers: </i> <br>
xxx-token: integer — токен авторизации <br>
xxx-userdata: integer — id пользователя <br>
<br>
<i> Response: </i> <br>
message: string — сообщение об ошибке/успехе <br>
success: boolean — удалено/не удалено <br>
<br>
<b> PUT </b> /reports/{report_id}  — изменить сообщение об ошибке <br>
<i> Path parameters: </i> <br>
report_id: int — id обращения <br>
<br>
<i> Headers: </i> <br>
xxx-token: integer — токен авторизации <br>
<br>
<i> Body parameters: </i> <br>
text: string — сообщение об ошибке <br>
user_id: int — id пользователя <br>
<br>
<i> Response: </i> <br>
text: string — текст сообщения в поддержку
status: boolean — обновлено/не обновлено
message: string — сообщение об ошибке/успехе <br>
<br>

## Тестирование API
<b> GET /programs </b><br>
```
pm.test("Verify status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Success response", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.offset).to.eql(10);
    pm.expect(jsonData.programs.length).to.eql(20);
});
```
![plot](Screenshots/programs1.png)
<br>
![plot](Screenshots/programs2.png)
<br>
<b> POST /users/create </b><br>
Тестируется невозможность создать пользователя с тем же именем
```
pm.test("Verify status code is 400", function () {
    pm.response.to.have.status(400);
});

pm.test("Message 9s Username already used", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.message).to.eql("Username already used");
    pm.expect(jsonData.username).to.eql("MasterX");
});
```
![plot](Screenshots/users_create1.png)
<br>
![plot](Screenshots/users_create2.png)
<br>
<b> POST /users/login </b><br>
```
pm.test("Verify status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Check if logged in", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.message).to.eql("Logged in");
    pm.expect(jsonData.username).to.eql("MasterX");
});
```
![plot](Screenshots/users_login1.png)
<br>
![plot](Screenshots/users_login2.png)
<br>
<b> GET /users/{username}/reports </b><br>
```
pm.test("Verify status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Success response", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.status).to.eql(true);
    pm.expect(jsonData.reports.length).to.eql(2);
});
```
![plot](Screenshots/user_reports1.png)
<br>
![plot](Screenshots/user_reports2.png)
<br>
<b> POST /reports </b><br>
```
pm.test("Verify status code is 201", function () {
    pm.response.to.have.status(201);
});

pm.test("Check if posted", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.text).to.eql("Eh bien mon prince");
    pm.expect(jsonData.message).to.eql("Posted");
});
```
![plot](Screenshots/post1.png)
<br>
![plot](Screenshots/post2.png)
<br>
![plot](Screenshots/post3.png)
<br>
<b> GET /reports/{username} </b><br>
```
pm.test("Verify status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Check length", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.status).to.eql(true);
    pm.expect(jsonData.reports.length).to.eql(2);
});
```
![plot](Screenshots/reports1.png)
<br>
![plot](Screenshots/reports2.png)
<br>
<b> DELETE /reports/{report_id} </b><br>
```
pm.test("Verify status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Check if deleted", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.message).to.eql("Deleted");
});
```
![plot](Screenshots/delete_report1.png)
<br>
![plot](Screenshots/delete_report2.png)
<br>
<b> PUT /reports/{report_id} </b><br>
```
pm.test("Verify status code is 202", function () {
    pm.response.to.have.status(202);
});

pm.test("Check if updated", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.message).to.eql("Updated");
});
```
![plot](Screenshots/reports_put1.png)
<br>
![plot](Screenshots/reports_put2.png)
<br>

## Дополнительно
Более подробное описание потоков сообщений для реализованных методов в [Swagger](openapi.yaml). <br>
Разработанные endpoint можно увидеть [здесь](../src/__main__.py). <br>
Для валидации данных и форматирования данных используются возможность фреймворков FastAPI и Pydantic. <br>
В ходе тестирования удалось найти ошибки, исправленные впоследствии. Набор тестов приложен в виде [коллеции Postman](postman_collection.json). <br>
[Скриншоты тестирования](Screenshots).


