from crypt import methods
from urllib.parse import parse_qs

from odoo import http
from odoo.http import request
import json
from .valid_response import valid_response

class GetAllOwnersController(http.Controller):

    # Get All Owners
    @http.route("/api/get/owners", methods=["GET"], type="http", auth="none", csrf=False)
    def get_owners(self):
        params = parse_qs(request.httprequest.query_string.decode('utf-8'))
        # print(params)
        owner_domain = []
        if params.get('name'):
            owner_domain += [('name', '=', params.get('name')[0])]
        # print(params.get('name')[0])
        owners = request.env['owner'].sudo().search(owner_domain)
        print(owners)
        if not owners:
            return valid_response("","There are no records !",404)

        response_body = [{
            "id": owner.id,
            "name": owner.name,
        } for owner in owners]

        return valid_response(response_body,"",200)
