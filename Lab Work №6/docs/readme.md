# Разработка BI-системы для исследования учебных планов образовательных программ университетов

## Gang of Four Patterns
### Порождающие паттерны
#### Factory
Используется для порождения парсеров учебных планов, реализующих ParserProtocol. Парсеры резолвятся с помощью встроенного в ParserFactory словаря с возможными парсерами.

![plot](./Images/Factory.png)

```
class ParserProtocol(Protocol):
    
    @abstractmethod
    def parse(self, payload) -> dict:
        raise NotImplementedError

class ParserFactory:
    _parsers: Final = {
        "hse": {
            "basic": {
                "table": BasicHseParser
            },
            "anual": {
               AnualHseParser
            }
        },
        "psu": {
            PsuParser
        }
    }
    
    @staticmethod
    def choose_parser(data_type: str, university: str, plan_type: str) -> ParserProtocol:
        return ParserFactory._parsers[university][plan_type][data_type]()
```
#### Builder
Класс Query используется для создания запроса к базе данных с помощью ORM.
![plot](./Images/Builder.png)
```
programs_pre_query = session \
                                    .query(
                                           MVP_API.program_id,
                                           MVP_API.program_name,
                                           MVP_API.field_code,
                                           MVP_API.degree_id,
			                               Degree.name.label("degree_name")
			                        ) \
                                    .filter(MVP_API.degree_id==Degree.id) \
                                    .offset(offset) \
                                    .limit(limit) \
        # Тут может добавиться код
        programs = programs_pre_query.all() # выполняется собранный запрос
```
#### Prototype
Представим метод для создания объекта AuthData, используемый при авторизации, на основе существующего. В Python методы __copy__ и __deepcopy__ зашиты на уровне языка, поэтому в данном примере их наследование опущено.

![plot](./Images/Prototype.png)
```
class AuthData:

    def __init__(self,
                 uuid: str,
                 username: str,
                 token: str,
                 created_at: datatime):

        self._uuid = uuid
	self._username = username
	self._token = token
	self._created_at = created_at

    def __copy__(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        return result

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, deepcopy(v, memo))
        return result
```

### Структурные паттерны
#### Decorator
На настоящий момент Decorator в его чистом виде используется редко, вместо это зачастую используют его функциональную альтернативу. Аннотация get принимает внутрь себя метод, который корректирует поведение вложенного метода.

![plot](./Images/Decorator.png)
```
@app.get("/programs/fields",
         summary="Список направлений подготовки",
         description="""Список направлений подготовки, для которых найдены программы""",
)
def get_field_codes() -> FieldsResponse:
    field_codes_rows = select_fields()
    fields = fields_from_rows(field_codes_rows)
    return FieldsResponse(field_codes=fields)
```

#### Facade
Данный паттерн используется работе для упрощения запросов к базе данных

![plot](./Images/Facade.png)
```
class Queries:
	def select_programs(filter: Optional[dict[str, list]]=None,
	                    session_maker: sessionmaker[Session]=SessionMaker,
			    offset: int=0,
			    limit: int=20):
	# Query

class FieldsRequests:
	def get_fields(authorization):
	    
	    fields = request(
	            headers={"Authorization": authorization},
	            method="GET",
	            url=fields_url
	            )
	    return fields


class ProgramsRowsConverter:
	def programs_from_rows(programs_rows, fields) -> list[Program]:
	    
	    return [Program(
	                    program_id=p.program_id,
	                    program_name=p.program_name,
	                    degree_id=p.degree_id,
	                    degree=p.degree_name,
	                    field_code=p.field_code,
	                    field_name=fields[p.field_code]["field_name"],
	                    field_group_code=fields[p.field_code]["field_group_code"],
	                    field_group_name=fields[p.field_code]["field_group_name"]
	                   )
	            for p
	            in programs_rows
	    if p.field_code in fields.keys()]

class ProgramQueryAdapter:
	def get_programs(authorization, offset, limit):
            programs_rows = select_programs(offset=args.offset,
		                            limit=args.limit)
            fields = {f["field_code"]: f 
	              for f 
	              in get_fields(authorization).json()}
            return ProgramsRowsConverter().programs_from_rows(programs_rows, fields)
```
