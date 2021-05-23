from odoo import api, fields, models
from odoo.exceptions import UserError


# this is a class for the hospital patient


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Patient Details"
    name = fields.Char(string='Name', required=True, tracking=True)
    middle_name = fields.Char(string='Middle Name', tracking=True)
    family_name = fields.Char(string="Family Name", tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], tracking=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('cancel', 'Canceled'),
        ('done', 'Done')],
        string='Status', default='draft', readonly=False, tracking=True
    )
    responsible_id = fields.Many2one('res.partner', string="Responsible")

    note = fields.Text(string='Description', tracking=True)

    def action_confirm(self):
        print("button pressed")
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'

    def action_set_draft(self):
        self.state = 'draft'

    def action_cancel(self):
        self.state = 'cancel'

    @api.model
    def create(self, values):
        if not values.get('note'):
            values['note'] = "New Patient"
        return super(HospitalPatient, self).create(values)

    def unlink(self):
        for hospitalPatient in self:
            if hospitalPatient.state == 'confirm':
                raise UserError('You cannot delete this record because it is confirmed')
        return super(HospitalPatient, self).unlink()
