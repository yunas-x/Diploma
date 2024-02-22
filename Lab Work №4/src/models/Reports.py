from pydantic import BaseModel
from ...loaders.orm.Queries import Queries
from ...loaders.orm.ORMStatus import ORMStatus
from ...loaders.Context import SessionMaker
from ...loaders.models.Report import Report as ReportORMModel

from datetime import datetime

class Report(BaseModel):
    text: str

class DeleteReportRequest(BaseModel):
    user_id: int
    
class ReportResponse(Report):
    id: int
    posted_on: datetime

class ReportRequest(Report):
    user_id: int
    
class ReportsResponse(BaseModel):
    status: bool
    user_id: int|None
    reports: list[ReportResponse]|None
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
        return ReportsResponse(user_id=None, reports=None, message="No such user", status=False)
    reports = Queries(SessionMaker).get_reports_by_userid(user_id=id)
    reports_list = [ReportResponse(text=r.text,
                                   id=r.id, 
                                   posted_on=r.posted_on) 
                   for r in reports]
    return ReportsResponse(user_id=id, reports=reports_list, message="Success", status=True)

def check_report(id: int, user_id: int):
    status = Queries(SessionMaker) \
                        .check_report_is_owned_by_user(id=id, user_id=user_id)
    return status

def delete_report_by_id(id: int) -> DeleteResponse:
    status = Queries(SessionMaker).delete_report_by_id(id=id)
    return DeleteResponse(message=delete_status_mapping[status], 
                          status=status)
    
def update_report_by_id(id: int, text: str) -> UpdateResponse:
    status = Queries(SessionMaker).update_report_by_id(id=id, text=text)
    return UpdateResponse(text=text, 
                          message=update_status_mapping[status],
                          status=status)
    
def add_report(report: ReportRequest) -> UpdateResponse:
    model = ReportORMModel(user_id=report.user_id,
                           text=report.text)
    
    status = Queries(SessionMaker).add(model)
    return UpdateResponse(text=report.text, 
                          message=post_status_mapping[status==ORMStatus.OK],
                          status=status==ORMStatus.OK)
    
