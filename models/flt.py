from odoo import api, fields, models, _
from odoo.addons.http_routing.models.ir_http import slug
from odoo.exceptions import UserError


class FltCategory(models.Model):
    _name = 'sanergy.flt.category'
    _description = 'FLT category'

    name = fields.Char('Category', required=True)

class FltRoute(models.Model):
    _name = 'sanergy.flt.route'
    _description = 'FLT Route'

    name = fields.Char('Route', required=True)
    crew_lead1_id = fields.Many2one('hr.employee', string='Crew Lead 1')
    crew_lead2_id = fields.Many2one('hr.employee', string='Crew Lead 2')

class FltCollector(models.Model):
    _name = 'sanergy.flt.collector'
    _description = 'Collector'

    employee_id = fields.Many2one('hr.employee', string='Employee')
    route_id = fields.Many2one('sanergy.flt.route', string='Collection Route')
    supervisor_id = fields.Many2one('hr.employee', string='Supervisor')
    status = fields.Selection([('active', 'Active'), ('inactive', 'In Active')], default='active')

class Flt(models.Model):
    _name = 'sanergy.flt'
    _description = 'Fresh life toilets'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Toilet Name', required=True)
    category_id = fields.Many2one('sanergy.flt.category', string='Category')
    route_id = fields.Many2one('sanergy.flt.route', string='Collection Route')
    location = fields.Char('Location')
    date_opened = fields.Date('Date Opened')    
    date_closed = fields.Date('Date Closed', readonly=True)
    current_status = fields.Selection([('open', 'Open'), ('closed', 'Closed')], readonly=True, default='open', tracking=True)
    status_lines = fields.One2many('sanergy.flt.status', 'flt_id', string='Status Lines', copy=True, auto_join=True)

    def action_close_flt(self):
        if self.current_status != 'open':
            raise UserError("You can not close an already closed FLT")
        self.write({
            'current_status': 'closed',
            'date_closed': fields.Date.today(),
        })

    def action_reopen_flt(self):
        if self.current_status != 'closed':
            raise UserError("You can not open an open FLT")
        self.write({
            'current_status': 'open',
            'date_opened': fields.Date.today(),
            'date_closed': None,
        })
        #write to status table
        vals = {
                'flt_id': self.id,
                'comment': None,
                'updated_type': None,
                'status': 'open',
            }
        self.env['sanergy.flt.status'].create(vals)

    class FltStatus(models.Model):
        _name = 'sanergy.flt.status'
        _description = 'Fresh life toilet status'

        flt_id = fields.Many2one(
            'sanergy.flt', string='FLT', required=True,
            default=lambda self: self.env.context.get('active_id', None),
        )
        updated_type = fields.Selection([('temporary', 'Temporary'), ('permanent', 'Permanent')], default='temporary')
        status = fields.Selection([('open', 'Open'), ('closed', 'Closed')], default='closed')
        comment = fields.Text('Comment')

