from odoo import api, fields, models, _
from odoo.exceptions import UserError


# this is a class for the hospital patient


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Patient Details"
    _order = "reference desc"

    name = fields.Char(string='Name', required=True, tracking=True)
    reference = fields.Char(string='Reference', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    middle_name = fields.Char(string='Middle Name', tracking=True)
    family_name = fields.Char(string="Family Name", tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], tracking=True, default="male", required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('cancel', 'Canceled'),
        ('done', 'Done')],
        string='Status', default='draft', readonly=False, tracking=True
    )
    responsible_id = fields.Many2one('res.partner', string="Responsible")

    note = fields.Text(string='Description', tracking=True)

    appointment_count = fields.Integer(string="No. Appointments", compute="_compute_appointment_count")

    height = fields.Float(string="Height(m)")
    weight = fields.Float(string="Weight(kg)")
    bmi = fields.Float(string="BMI", compute="_compute_bmi")
    image = fields.Binary(string="Patient Image")

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_set_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'

    def _compute_appointment_count(self):
        # we need to initiate an instance of the class hospital.appointment and search inside it the patient id
        for record in self:
            appointment_count = record.env['hospital.appointment'].search_count([("patient_id", "=", record.id)])
            record.appointment_count = appointment_count

    def _compute_bmi(self):
        for rec in self:
            if rec.height and rec.weight:
                rec.bmi = rec.weight / rec.height ** 2
            else:
                rec.bmi = 0.0

    @api.model
    def create(self, vals):
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.patient') or _('New')
        if not vals.get('note'):
            vals['note'] = "New Patient"
        return super(HospitalPatient, self).create(vals)

    def unlink(self):
        for hospitalPatient in self:
            if hospitalPatient.state == 'confirm':
                raise UserError('You cannot delete this record because it is confirmed')
        return super(HospitalPatient, self).unlink()

    @api.model
    def default_get(self, fields):
        """ This is a default function to get the values for the gender as well as the New field
        """

        res = super(HospitalPatient, self).default_get(fields)
        print(fields)
        res['gender'] = 'other'
        print(res['gender'])
        return res
