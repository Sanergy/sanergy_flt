from odoo import api, fields, models, _
from odoo.exceptions import UserError

class UpdateStatus(models.TransientModel):
    _name = 'sanergy.flt.status.update'
    _description = 'Fresh life toilet status'

    flt_id = fields.Many2one(
        'sanergy.flt', string='FLT', required=True,
        default=lambda self: self.env.context.get('active_id', None),
    )
    date_closed = fields.Date('Date Closed', default=fields.Date.today())
    #closed_by = fields.Many2one('res.users', string='Closed By', index=True, required=True, default=lambda self: self.env.user)
    closure_type = fields.Selection([('temporary', 'Temporary'), ('permanent', 'Permanent')], default='temporary')
    status = fields.Selection([('open', 'Open'), ('closed', 'Closed')], default='closed')
    reason = fields.Text('Reason for closure')

    def action_flt_close(self):
        vals = {
                'flt_id': self.flt_id.id,
                'comment': self.reason,
                'updated_type': self.closure_type,
                'status': 'closed',
            }
        self.env['sanergy.flt.status'].create(vals)

        flt = self.env['sanergy.flt'].browse(self.env.context.get('active_id'))
        flt.write({
            'current_status': 'closed',
            'date_closed': fields.Date.today(),
        })

    

