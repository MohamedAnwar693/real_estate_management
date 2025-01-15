from odoo import models, fields

class Tenant(models.Model):
    _name = 'tenant.real.estate'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'Tenant'

    name = fields.Char(string='Tenant Name', required=True, tracking=True)
    phone = fields.Char(string='Phone Number', tracking=True)
    email = fields.Char(string='Email', required=True, tracking=True)
    leases = fields.One2many('lease.real.estate', 'tenant_id', string='Leases', tracking=True)
    profile_picture = fields.Binary('Profile Picture')
    occupation = fields.Char('Occupation', tracking=True)
    birthdate = fields.Date('Birthdate', tracking=True)