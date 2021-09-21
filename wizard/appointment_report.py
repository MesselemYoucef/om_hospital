from odoo import api, fields, models, _

class AppointmentReport(models.TransientModel):
    _name = "appointment.report.wizard"
    _description = "Wizard that falicitates retrieving appointments"

    date_from = fields.Date(string="From", required=False)
    date_to = fields.Date(string="To", required=False)
    patient_id = fields.Many2one("hospital.patient", string="Patient Name", required=False)

    def action_print_report(self):
        patient_id = self.read()[0].get('patient_id')
        if patient_id:
            domain += [
                ('patient_id', '=', patient_id[0])
            ]
        appointments = self.env['hospital.appointment'].search_read([('patient_id', '=', self.patient_id.id)])
        data = {
            'form': self.read()[0],
            'appointments': appointments
        }
        return self.env.ref('om_hospital.action_report_appointment').report_action(self, data=data)
