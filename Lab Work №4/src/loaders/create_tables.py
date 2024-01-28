from models.Competence import Competence
from models.Course import Course
from models.Curricula import Curricula
from models.Degree import Degree
from models.Faculty import Faculty
from models.FieldOfStudy import FieldOfStudy
from models.Program import Program
from models.University import University
from models.Intermediate import Intermediate
from models.IntermediateValues import IntermediateValues
from models.User import User
from models.Report import Report
from Context import Engine


if __name__ == "__main__":
    Competence.metadata.create_all(bind=Engine)
    Course.metadata.create_all(bind=Engine)
    Degree.metadata.create_all(bind=Engine)
    Faculty.metadata.create_all(bind=Engine)
    FieldOfStudy.metadata.create_all(bind=Engine)
    Program.metadata.create_all(bind=Engine)
    University.metadata.create_all(bind=Engine)
    Curricula.metadata.create_all(bind=Engine)
    Intermediate.metadata.create_all(bind=Engine)
    IntermediateValues.metadata.create_all(bind=Engine)
    User.metadata.create_all(bind=Engine)
    Report.metadata.create_all(bind=Engine)