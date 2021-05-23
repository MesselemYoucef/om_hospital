from odoo import api, fields, models

# this is a class for the hospital patient


class SalesOrder(models.Model):
    _inherit = "sale.order"
    sale_description = fields.Char(string='Sale Description', required=False)
