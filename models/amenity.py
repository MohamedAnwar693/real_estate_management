from odoo import models, fields

class Amenity(models.Model):
    _name = 'amenity.real.estate'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'Property Amenity'

    name = fields.Char('Amenity Name', required=True, tracking=True)
    description = fields.Text('Description', tracking=True)
