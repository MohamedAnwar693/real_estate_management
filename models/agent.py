from odoo import models, fields

class Agent(models.Model):
    _name = 'agent.real.estate'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'Agent'

    image = fields.Image(readonly=False)
    name = fields.Char(string='Agent Name', required=True)
    phone = fields.Char(string='Phone Number', tracking=True)
    email = fields.Char(string='Email', tracking=True)
    properties = fields.One2many('property.real.estate', 'agent_id', string='Properties', tracking=True)
    agency_name = fields.Char('Agency Name', tracking=True)
    years_experience = fields.Integer('Years of Experience', tracking=True)
    profile_picture = fields.Binary('Profile Picture')