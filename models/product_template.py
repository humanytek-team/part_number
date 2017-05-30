from openerp import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    part_number = fields.Char(
        string='part_number',
    )
