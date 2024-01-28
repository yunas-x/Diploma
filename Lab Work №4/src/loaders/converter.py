import os
import json
from datetime import date

from Context import SessionMaker
from models.Intermediate import Intermediate
from orm.Queries import Queries

dir_path = r"C:/good"

jsons = [file for file in os.listdir(dir_path) if file.endswith(".json")]
queries = Queries(SessionMaker)

for json_ in jsons:
    filename = os.path.join(dir_path, json_)
    with open(filename, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except:
            continue
    for field in data["ProgramInfo"]["fields_of_study"]:
        for course in data["ProgramInfo"]["courses"]:
            for competence in course["competences"]:
                intermediate = Intermediate(
                    course_name=course["name"],
                    type_=course["type"],
                    added=date.today(),
                    removed=None,
                    code=competence["code"],
                    competence_type=competence["type"],
                    program_name=data["ProgramInfo"]["name"],
                    degree_id=data["ProgramInfo"]["degree"]["code"],
                    field_code=field["code"],
                    university_id=1,
                    credits=course["credits"],
                    enrollment_year=data["ProgramInfo"]["yearEnrolled"],
                    year=course["year"]
                )
                
                status = queries.add(intermediate)
                print(status)