from odoo import api, fields, models


class CreateAppointmentWizard(models.TransientModel):
    _name = "create.appointment.wizard"
    _description = "Module to create an appointment wizard"

    appointment_date = fields.Datetime(string="Appointment Date", required=True)
    patient_id = fields.Many2one("hospital.patient", string="Patient", required=True)

    def action_create_appointment(self):
        print("Button create has been pushed")
        vals={
            'patient_id': self.patient_id.id,
            'appointment_date': self.appointment_date
        }

        # create objest for the model hospital.appointment and called the create method
        self.env['hospital.appointment'].create(vals)
        print(vals)
