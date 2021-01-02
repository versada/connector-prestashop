# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class PrestashopBackend(models.Model):
    _name = "prestashop.backend"
    _inherit = ["prestashop.backend", "server.env.mixin"]

    @property
    def _server_env_fields(self):
        base_fields = super()._server_env_fields
<<<<<<< HEAD
        presta_fields = {
            "location": {},
            "webservice_key": {},
        }
        presta_fields.update(base_fields)
        return presta_fields
=======
        mail_fields = {
            "location": {},
            "webservice_key": {},
        }
        mail_fields.update(base_fields)
        return mail_fields
>>>>>>> Add connector_prestashop_environment

    @api.model
    def _server_env_global_section_name(self):
        """Name of the global section in the configuration files
        Can be customized in your model
        """
        return "prestashop"
