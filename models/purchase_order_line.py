from openerp import api, fields, models


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    part_number = fields.Char(
        readonly=True,
        related="product_id.part_number",
    )
