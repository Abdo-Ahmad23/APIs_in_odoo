from crypt import methods
from urllib.parse import parse_qs

from odoo import http
from odoo.http import request
import json
from .valid_response import valid_response
class GetSpecificOwnerController(http.Controller):

    # Get a specific Owner
    @http.route("/api/get/owner/<int:owner_id>", methods=["GET"], type="http", auth="none", csrf=False)
    def update_owner(self, owner_id):
        owner_id = request.env['owner'].sudo().search([('id', '=', owner_id)])

        try:
            if not owner_id:
                return valid_response("","This record is not exist",404)

            return valid_response({
                "id": owner_id.id,
                "name": owner_id.name,

            },"success fetch",200)

        except Exception as error:
            return request.make_json_response({
                "error": error
            })



