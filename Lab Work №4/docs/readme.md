# Разработка BI-системы для исследования учебных планов образовательных программ университетов

API к хранилищу данных для облегчения сравнения образовательных программ и их выбора абитуриентом. Выполняется в рамках комадного проекта и дипломного проекта в НИУ ВШЭ Пермь в рамках обучения на программной инженерии.

## Описание ресурсов
Ниже приведен список планируемых ресурсов и endpoint'ов. Часть из них не реализованы. К реализованным дано краткое пояснение, более подробную информацию, в том числе возвращаемые данные, можно найти в Swagger. Все параметры обязательны, если не указано иное.

### /programs — программы высшего образования
<b> GET </b> /programs — получить все программы высшего образования <br>
<b> IN: </b> <br>
<i> Query parameters: </i> <br>
offset: integer — номер строки, с которой возвращаются записи из базы данных, по умолчанию равен 0. Можно использовать для пагинации. <br>
<br>
<b> GET </b> /programs/{program_id}/ — получить данные по программе <br>
<b> GET </b> /programs/{program_id}/courses — получить список курсов для выбранной программы <br>
<b> POST </b> /programs/compare — сравнить несколько курсов <br>

### /users — пользователи
<b> POST </b> /users/create — создать пользователя <br>
<b> IN: </b> <br>
<i> Body parameters: </i> <br>
username: string (english) — имя пользователя <br>
email: string (email) — E-Mail <br>
password: string (english) — пароль <br>
<br>
<b> POST </b> /users/login — войти в систему <br>
<b> IN: </b> <br>
<i> Body parameters: </i> <br>
username: string (english) — имя пользователя <br>
password: string (english) — пароль <br>
<br>
<b> GET </b> /users/{username}/reports — все обращения пользователя <br>
<b> IN: </b> <br>
<i> Path parameters: </i> <br>
username: string (english) — имя пользователя <br>
<i> Headers: </i> <br>
xxx-token: integer — токен авторизации <br>

### /reports — сообщения об ошибках
<b> POST </b> /reports — отправить сообщение об ошибке <br>
<b> IN: </b> <br>
<i> Body parameters: </i> <br>
<br>
<b> GET </b> /reports/{username} — получить все сообщения об ошибке от пользователя <br>
<b> IN: </b> <br>
<i> Body parameters: </i> <br>
<br>
<b> DELETE </b> /reports/{report_id} — удалить сообщение об ошибке <br>
<b> IN: </b> <br>
<i> Body parameters: </i> <br>
<br>
<b> PUT </b> /reports/{report_id}  — изменить сообщение об ошибке <br>
<b> IN: </b> <br>
<i> Body parameters: </i> <br>
<br>

Более подробное описание потоков сообщений для реализованных методов в [Swagger](openapi.yaml). <br>
Разработанные endpoint можно увидеть [здесь](../src/__main__.py). <br>
Для валидации данных и форматирования данных используются возможность фреймворков FastAPI и Pydantic. <br>

В ходе тестирования удалось найти ошибки, исправленные впоследствии. Набор тестов приложен в виде [коллеции Postman](postman_collection.json). <br>
[Скриншоты тестирования](Screenshots).


