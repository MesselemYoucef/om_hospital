from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError


# this is a class for the hospital patient


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Appointments for the patients"
    _order = "reference desc"
    _rec_name = "reference"

    reference = fields.Char(string='Reference',
                            required=True,
                            copy=False,
                            readonly=True,
                            default=lambda self: _('New'))
    patient_id = fields.Many2one('hospital.patient',
                                 string="Patient Name",
                                 required=True, stored=True)
    # This is a selection field
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('cancel', 'Canceled'),
        ('done', 'Done')],
        string='Status', default='draft', readonly=False, tracking=True
    )

    note = fields.Text(string='Description', tracking=True)
    prescription = fields.Text(string='Prescription', tracking=True)
    prescription_line_ids = fields.One2many('appointment.prescription.lines', 'appointment_id',
                                            String="Prescription Lines")
    appointment_date = fields.Datetime(string="Appointment Date")
    age = fields.Integer(string='Age', related='patient_id.age', tracking=True )
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], tracking=True)
    doctor_id = fields.Many2one("hospital.doctor", string="Doctor", required=True)

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

    def unlink(self):
        for record in self:
            if record.state == "confirm" or record.state == "done":
                raise ValidationError_  ("You cannot delete record %s in state " % self.reference)
        return super(HospitalAppointment, self).unlink()


class AppointmentPrescriptionLines(models.Model):
    _name = "appointment.prescription.lines"
    _description = "Appointment Prescription Lines"

    name = fields.Char(string="Medicine", required=True)
    qty = fields.Integer(string="Quantity")
    appointment_id = fields.Many2one('hospital.appointment', String="Appointment")
    # appointment_reference = fields.Char(Related="appointment_id.reference", String="Appointment")







