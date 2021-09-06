from odoo import api, fields, models, _
from odoo.exceptions import UserError

class FltStatus(models.TransientModel):
    _name = 'sanergy.flt.status'
    _description = 'Fresh life toilet status'

    flt_id = fields.Many2one(
        'sanergy.flt', string='FLT', required=True,
        default=lambda self: self.env.context.get('active_id', None),
    )
    date_closed = fields.Date('Date Closed', default=fields.Date.today())
    closed_by = fields.Many2one('res.users', string='Closed By', index=True, required=True, default=lambda self: self.env.user)
    closure_type = fields.Selection([('temporary', 'Temporary'), ('permanent', 'Permanent')], default='temporary')
    status = fields.Selection([('open', 'Open'), ('closed', 'Closed')], default='closed')
    reason = fields.Text('Reason for closure')

    def action_close_flt(self):
        if self.current_status != 'open':
            raise UserError("You can not close an already closed FLT")
        self.write({
            'status': 'closed',
            'date_closed': fields.Date.today(),
        })

    def action_open_flt(self):
        if self.current_status != 'open':
            raise UserError("You can not close an already closed FLT")
        self.write({
            'status': 'open',
            'date_closed': None,
        })