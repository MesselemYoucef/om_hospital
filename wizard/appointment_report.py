from odoo import api, fields, models, _

class AppointmentReport(models.TransientModel):
    _name = "appointment.report.wizard"
    _description = "Wizard that falicitates retrieving appointments"

    date_from = fields.Datetime(string="From", required=False)
    date_to = fields.Datetime(string="To", required=False)
    patient_id = fields.Many2one("hospital.patient", string="Patient Name", required=False)

    def action_print_report(self):
        domain = []
        patient_id = self.patient_id
        if patient_id:
            domain += [('patient_id', '=', patient_id.id)]
        date_from = self.date_from
        date_to = self.date_to
        if date_from:
            domain += [('appointment_date', '>=', date_from)]
        if date_to:
            domain += [('appointment_date', '<=', date_to)]

        appointments = self.env['hospital.appointment'].search_read(domain)
        data = {
            'form': self.read()[0],
            'appointments': appointments
        }
        return self.env.ref('om_hospital.action_report_appointment').report_action(self, data=data)
