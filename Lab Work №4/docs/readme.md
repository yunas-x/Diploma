# Разработка BI-системы для исследования учебных планов образовательных программ университетов

API к хранилищу данных для облегчения сравнения образовательных программ и их выбора абитуриентом. Выполняется в рамках комадного проекта и дипломного проекта в НИУ ВШЭ Пермь в рамках обучения на программной инженерии.

## Документация по API
Ниже приведен список планируемых ресурсов и endpoint'ов. Часть из них не реализованы. К реализованным дано краткое пояснение, более подробную информацию, в том числе возвращаемые данные, можно найти в Swagger. Все параметры обязательны, если не указано иное.

### /programs — программы высшего образования
<table>
  <tr>
    <td colspan="2"><b> GET </b> /programs — получить все программы высшего образования<td>
  </tr>
  <tr>
    <td><i> Query parameters: </i></td>
    <td><i> Response: </i></td>
  </tr>
  <tr>
    <td>
      <b>offset</b>: integer — номер строки, с которой возвращаются записи из базы данных, по умолчанию равен 0. Можно использовать для пагинации
    </td>
    <td rowspan="2">
      <b>programs</b>: array[Program] — Список программ высшего образования <br>
      <br>
      <b>Program</b> { <br>
        program_name: string — название программы <br>
        degree_id: integer — уровень обучения <br>
        field_code: string — направление подготовки (Код ОК 009-2016) <br>
        university_id: integer — ID университета <br>}
    </td>
  </tr>
  <tr>
    <td><b>limit</b>: integer — количество возвращаемых записей</td>
  </tr>
</table>

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
<i> Redirect on: </i> <b> GET </b> /reports/{username} <br>

### /reports — сообщения об ошибках
Данные запросы завершаются ошибкой при неверных данных пользователя (id или имя пользователя) и токенах авторизации. <br>
При попытке манипуляции с сообщениями проверяется принадлежность токена пользователю. <br>

<b> POST </b> /reports — отправить сообщение об ошибке <br>
<i> Body parameters: </i> <br>
text: string — сообщение об ошибке <br>
user_id: int — id пользователя <br>
<i> Headers: </i> <br>
xxx-token: integer — токен авторизации <br>
<i> Response: </i> <br>
text: string — текст сообщения в поддержку <br>
message: string — сообщение об ошибке/успехе <br>
success: boolean — создано/не создано <br>
<br>
<b> GET </b> /reports/{username} — получить все сообщения об ошибке от пользователя <br>
<i> Path parameters: </i> <br>
username: string (english) — имя пользователя <br>
<i> Headers: </i> <br>
xxx-token: integer — токен авторизации <br>
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
<i> Headers: </i> <br>
xxx-token: integer — токен авторизации <br>
xxx-userdata: integer — id пользователя <br>
<i> Response: </i> <br>
message: string — сообщение об ошибке/успехе <br>
success: boolean — удалено/не удалено <br>
<br>
<b> PUT </b> /reports/{report_id}  — изменить сообщение об ошибке <br>
<i> Path parameters: </i> <br>
report_id: int — id обращения <br>
<i> Headers: </i> <br>
xxx-token: integer — токен авторизации <br>
<i> Body parameters: </i> <br>
text: string — сообщение об ошибке <br>
user_id: int — id пользователя <br>
<i> Response: </i> <br>
text: string — текст сообщения в поддержку
status: boolean — обновлено/не обновлено
message: string — сообщение об ошибке/успехе <br>
<br>

Более подробное описание потоков сообщений для реализованных методов в [Swagger](openapi.yaml). <br>
Разработанные endpoint можно увидеть [здесь](../src/__main__.py). <br>
Для валидации данных и форматирования данных используются возможность фреймворков FastAPI и Pydantic. <br>

В ходе тестирования удалось найти ошибки, исправленные впоследствии. Набор тестов приложен в виде [коллеции Postman](postman_collection.json). <br>
[Скриншоты тестирования](Screenshots).


