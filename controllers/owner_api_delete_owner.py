
from odoo import http
from odoo.http import request
from .valid_response import valid_response

class DeleteOwnerController(http.Controller):


    @http.route("/api/delete/owner/<int:owner_id>", methods=["DELETE"], type="http", auth="none", csrf=False)
    def delete_owner(self, owner_id):
        owner_id = request.env['owner'].sudo().search([('id', '=', owner_id)])
        try:
            if not owner_id:
                return valid_response("","This record is not exist !",404)

            owner_id.unlink()
            return valid_response("", "Deleted has been successfully", 200)

        except Exception as error:
            return request.make_json_response({
                "error": error
            })


