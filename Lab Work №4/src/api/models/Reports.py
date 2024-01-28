from pydantic import BaseModel
from ...loaders.orm.Queries import Queries
from ...loaders.Context import SessionMaker
from ...loaders.models.Report import Report as ReportORMModel

class Report(BaseModel):
    text: str
    
class ReportRequest(Report):
    user_id: int
    
class ReportsResponse(BaseModel):
    status: bool
    user_id: int|None
    reports: list[Report]|None
    message: str
    
class DeleteResponse(BaseModel):
    status: bool
    message: str
    
class UpdateResponse(Report):
    status: bool
    message: str
    
delete_status_mapping = {True: "Deleted", False: "Not Deleted. Try again"}
update_status_mapping = {True: "Updated", False: "Not Updated. Try again"}
post_status_mapping = {True: "Posted", False: "Not Posted. Try again"}
    
def get_reports_by_userid(id: int):
    if id is None:
        return ReportsResponse(user_id=None, reports=None, message="No such user")
    reports = Queries().get_reports_by_userid(user_id=id)
    reports_list = [Report(r.id, 
                   r.text, 
                   r.posted_on) 
                   for r in reports]
    return ReportsResponse(user_id=id, reports=reports, message="Success")

def delete_report_by_id(id: int) -> DeleteResponse:
    status = Queries().delete_report_by_id(id=id)
    return DeleteResponse(message=delete_status_mapping[status], 
                          status=status)
    
def update_report_by_id(id: int, text: str) -> UpdateResponse:
    status = Queries().update_report_by_id(id=id, text=text)
    return UpdateResponse(text=text, 
                          message=update_status_mapping[status],
                          status=status)
    
def add_report(report: ReportRequest) -> UpdateResponse:
    model = ReportORMModel(user_id=report.user_id,
                           text=report.text)
    
    status = Queries(SessionMaker).add(model)
    return UpdateResponse(text=report.text, 
                          message=post_status_mapping[status],
                          status=status)
    
