from odoo import api, fields, models, _

class AppointmentReport(models.TransientModel):
    _name = "appointment.report.wizard"
    _description = "Wizard that falicitates retrieving appointments"

    date_from = fields.Datetime(string="From", required=True)
    date_to = fields.Datetime(string="To", required=True)
    patient_id = fields.Many2one("hospital.patient", string="Patient Name", required=True)

