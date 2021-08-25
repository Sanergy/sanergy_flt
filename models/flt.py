from odoo import models, fields, api

class Flt(models.Model):
    _name = 'sanergy.flt'
    _description = 'Fresh life toilets'

    name = fields.Char('Toilet Name', required=True)
    location = fields.Char('Location')
    date_opened = fields.Date('Date Opened')
    date_closed = fields.Date('Date Closed')
    status = fields.Selection([('open', 'Open'), ('closed', 'Closed')], default='open')