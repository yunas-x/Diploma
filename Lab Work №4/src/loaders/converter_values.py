import os
import json

from Context import SessionMaker
from models.IntermediateValues import IntermediateValues
from orm.Queries import Queries

dir_path = r"C:/annual_jsons"

jsons = [file for file in os.listdir(dir_path) if file.endswith(".json")]
queries = Queries(SessionMaker)

for json_ in jsons:
    filename = os.path.join(dir_path, json_)
    with open(filename, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except:
            continue
    for course in data["ProgramInfo"]["courses"]:
        intermediate = IntermediateValues(
            course_name=course["name"],
            program_name=data["ProgramInfo"]["name"],
            enrollment_year=data["ProgramInfo"]["yearEnrolled"],
            year=course["year"],
            credits=course["credits"],
            classroom_hours=course["classroomHours"],
            readBy=course["readBy"]
        )
                
        status = queries.add(intermediate)
        print(status)