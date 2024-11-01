from odoo import http
from odoo.http import request
import json


def valid_response(data,message,status ):
    response_body = {
        'status':status,
        'message':message,
        'data':data
    }

    return request.make_json_response(response_body,status = status)
