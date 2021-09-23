from odoo import api, fields, models, _


class PatientReportWizard(models.TransientModel):
    _name = "patient.report.wizard"
    _description = "Print Patient Report Wizard"

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string="Gender")

    age = fields.Integer(string="Age")

    def action_print_report(self):
        data = {
            'form_data': self.read()[0],
        }
        return self.env.ref('om_hospital.action_report_patients').report_action(self, data=data)