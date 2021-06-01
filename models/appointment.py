from odoo import api, fields, models, _
from odoo.exceptions import UserError


# this is a class for the hospital patient


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Appointments for the patients"

    reference = fields.Char(string='Reference',
                            required=True,
                            copy=False,
                            readonly=True,
                            default=lambda self: _('New'))
    patient_id = fields.Many2one('hospital.patient',
                                 string="Patient Name",
                                 required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('cancel', 'Canceled'),
        ('done', 'Done')],
        string='Status', default='draft', readonly=False, tracking=True
    )

    note = fields.Text(string='Description', tracking=True)

    date_appointment = fields.Date(string="Date")
    date_appointment_checkup = fields.Datetime(string="Checkup")
    age = fields.Integer(string='Age', related='patient_id.age', tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], tracking=True)

    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'

    def action_set_draft(self):
        self.state = 'draft'

    def action_cancel(self):
        self.state = 'cancel'

    @api.model
    def create(self, vals):
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or _('New')
        return super(HospitalAppointment, self).create(vals)

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        """Observing the change of patient_id field"""
        if self.patient_id:
            if self.patient_id.gender:
                self.gender = self.patient_id.gender
        else:
            self.gender = ''

        if self.patient_id.note:
            self.note = self.patient_id.note
