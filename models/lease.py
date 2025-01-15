from odoo import models, fields

class Lease(models.Model):
    _name = 'lease.real.estate'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'Lease Agreement'

    property_id = fields.Many2one('property.real.estate', string='Property', required=True, tracking=True)
    tenant_id = fields.Many2one('tenant.real.estate', string='Tenant', required=True, tracking=True)
    start_date = fields.Date(string='Start Date', required=True, tracking=True)
    end_date = fields.Date(string='End Date', required=True, tracking=True)
    rent_amount = fields.Float(string='Rent', required=True, tracking=True)
