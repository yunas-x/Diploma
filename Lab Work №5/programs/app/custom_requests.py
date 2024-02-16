import os
from requests import request
import json

fields_url = os.environ['FIELDS_URL']
auth_url = os.environ['AUTH_URL']

def get_fields(authorization):
    
    fields = request(
            headers={"Authorization": authorization},
            method="GET",
            url=fields_url
            )
    return fields

def auth(session_id: str):
    fields = request(
        method="POST",
        url=auth_url,
        data=session_id
    )
    return fields.status_code == 200
