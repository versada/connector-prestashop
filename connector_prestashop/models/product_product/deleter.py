# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo.addons.component.core import Component


class ProductCombinationDelete(Component):
    _name = 'prestashop.product.combination.deleter'
    _inherit = 'prestashop.deleter'
    _apply_on = 'prestashop.product.combination'

    _model_name = 'prestashop.product.combination'

    def delete(self, id):
        """ Delete a record on the external system """
        return self._call('%s.delete' % self._prestashop_model, [int(id)])
