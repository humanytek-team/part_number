from openerp import api, fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    part_number = fields.Char()
