from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Property(models.Model):
    _name = 'property.real.estate'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'Property'

    name = fields.Char(string='Property Name', required=True, tracking=True)
    property_type_id = fields.Many2one('real.estate.property.type', string='Property Type', required=True, tracking=True)
    address = fields.Text(string='Address', tracking=True)
    city = fields.Char(string='City', tracking=True)
    state = fields.Many2one('res.country.state', string='State', required=True, tracking=True)
    zip_code = fields.Char('Zip Code', tracking=True)
    latitude = fields.Float('Latitude', tracking=True)
    longitude = fields.Float('Longitude', tracking=True)
    country_id = fields.Many2one('res.country', string='Country', tracking=True)
    price = fields.Float(string='Price', tracking=True)
    status = fields.Selection([
        ('available', 'Available'),
        ('pending', 'Pending'),
        ('sold', 'Sold'),
        ('rented', 'Rented')
    ], string='Status', default='available', tracking=True)
    area = fields.Float('Area (sqft)', required=True)
    num_rooms = fields.Integer('Number of bedrooms', tracking=True)
    num_bathrooms = fields.Integer('Number of Bathrooms', tracking=True)
    num_floors = fields.Integer('Number of Floors', tracking=True)
    amenities = fields.Many2many('amenity.real.estate', string='Amenities', tracking=True)
    #****************** Relationships***************
    agent_id = fields.Many2one('agent.real.estate', string='Agent', tracking=True)
    tenant_id = fields.Many2one('tenant.real.estate', string='Tenant', tracking=True)
    sale_id = fields.Many2one('sale.real.estate', string='Sale', tracking=True)
    lease_id = fields.Many2one('lease.real.estate', string='Lease', tracking=True)
    partner_id = fields.Many2one('res.partner', string='Partner', required=True, tracking=True)
    #************* Images***************
    image = fields.Binary('Property Image')
    pictures_of_property = fields.One2many('real.estate.property.image', 'property_id', string='Pictures Of Property')

    #*********** Customize Features**********
    condition = fields.Selection([
        ('new', 'New'),
        ('good', 'Good'),
        ('needs_renovation', 'Needs Renovation')
    ], string='Condition', required=True, tracking=True)


    @api.constrains('price')
    def _check_price_positive(self):
        for record in self:
            if record.price <= 0:
                raise ValidationError("Price must be grater that zero.")

    @api.model
    def create(self, vals):
        address = ''
        if vals.get('zip_code'):
            address += vals['zip_code']
        if vals.get('country_id'):
            country = self.env['res.country'].browse(vals['country_id'])
            address += ' - ' + country.name
        if vals.get('state'):
            state = self.env['res.country.state'].browse(vals['state'])
            address += ', ' + state.name
        if vals.get('address'):
            address += ', ' + vals['address']
        vals['address'] = address
        return super(Property, self).create(vals)


class PropertyType(models.Model):
    _name = 'real.estate.property.type'
    _description = 'Property Type'

    name = fields.Char(string='Type Name', required=True, tracking=True)

class PropertyImage(models.Model):
    _name = 'real.estate.property.image'
    _description = 'Property Image'

    image = fields.Binary('Image', required=True)
    description = fields.Char('Image Description')
    property_id = fields.Many2one('property.real.estate', string='Property', ondelete='cascade', tracking=True)