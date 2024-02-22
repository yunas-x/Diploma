import os
import json
from glom import glom

jsons = [file for file in os.listdir('.') if file.endswith(".json")]

for json_ in jsons:
    with open(json_, "r") as f:
        try:
            data = json.load(f)
        except:
            print(json_)
            continue
    competences = glom(data, ("ProgramInfo.courses", ["competences"]))
    are_not_empty = any(competences)
    if are_not_empty:
        os.rename(json_, f"./good/{json_}")