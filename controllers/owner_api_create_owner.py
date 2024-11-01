from crypt import methods
from urllib.parse import parse_qs

from odoo import http
from odoo.http import request
import json

from .valid_response import valid_response
class CreateOwnerController(http.Controller):


    @http.route("/api/create/owner", methods=["POST"], type="http", auth="none", csrf=False)
    def create_owner(self):
        args = request.httprequest.data.decode()
        vals = json.loads(args)
        res = request.env['owner'].sudo().create(vals)
        if res:
            return valid_response(vals,"Onwer field has been created successfully",200)

        else:
            return valid_response(vals,"This owner is not found !",404)

