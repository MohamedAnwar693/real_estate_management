from odoo import models, fields

class Sale(models.Model):
    _name = 'sale.real.estate'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'Sale'

    property_id = fields.Many2one('property.real.estate', string='Property', required=True, tracking=True)
    buyer_name = fields.Char(string='Buyer Name', required=True, tracking=True)
    sale_date = fields.Date(string='Sale Date', required=True, tracking=True)
    sale_price = fields.Float(string='Sale Price', required=True, tracking=True)
