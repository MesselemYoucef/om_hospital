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
        date_from = self.date_from
        date_to = self.date_to
        if patient_id:
            domain += [('patient_id', '=', patient_id.id)]
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

    def action_print_excel_report(self):
        domain = []
        patient_id = self.patient_id
        date_from = self.date_from
        date_to = self.date_to
        if patient_id:
            domain += [('patient_id', '=', patient_id.id)]
        if date_from:
            domain += [('appointment_date', '>=', date_from)]
        if date_to:
            domain += [('appointment_date', '<=', date_to)]
        appointments = self.env['hospital.appointment'].search_read(domain)
        data = {
            'appointments': appointments,
            'form_data': self.read()[0]
        }
        return self.env.ref('om_hospital.report_patient_appointment_xlsx').report_action(self, data=data)
