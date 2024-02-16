import os
from requests import request
import json

programs_url = os.environ['PROGRAMS_URL']
auth_url = os.environ['AUTH_URL']


def try_get_fields(authorization):
    
    fields_codes_filter = request(
            method="GET",
            headers={"Authorization": authorization},
            url=programs_url
        )
    
    return fields_codes_filter

def auth(session_id: str):
    fields = request(
        method="POST",
        url=auth_url,
        data=session_id
    )
    return fields.status_code == 200
