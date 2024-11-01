from crypt import methods
from urllib.parse import parse_qs

from odoo import http
from odoo.http import request
import json

from .valid_response import valid_response


class UpdateOwnerController(http.Controller):


    @http.route("/api/update/owner/<int:owner_id>",methods=["PUT"], type="http", auth="none", csrf=False)
    def update_owner(self,owner_id):
        owner_id = request.env['owner'].sudo().search([('id','=',owner_id)])
        args = request.httprequest.data.decode()
        vals = json.loads(args)
        owner_id.write(vals)
        try:
            if not owner_id:
                return valid_response(vals,"This record is not exist",404)

            return valid_response(vals,"Owner field has been updated successfully",200)

        except Exception as error:
            return request.make_json_response({
                "error":error
            })


