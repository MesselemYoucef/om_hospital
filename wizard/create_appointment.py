from odoo import api, fields, models, _


class CreateAppointmentWizard(models.TransientModel):
    _name = "create.appointment.wizard"
    _description = "Module to create an appointment wizard"


    @api.model
    def default_get(self, fields):
        """to get the default info when creating a new appointment"""
        res = super(CreateAppointmentWizard, self).default_get(fields)
        print(self._context)
        if self._context.get('active_id'):
            res['patient_id'] = self._context.get('active_id')
        return res

    appointment_date = fields.Datetime(string="Appointment Date", required=False)
    patient_id = fields.Many2one("hospital.patient", string="Patient", required=True)
    doctor_id = fields.Many2one("hospital.doctor", string="Doctor", required=True)

    def action_create_appointment(self):
        values = {
            'patient_id': self.patient_id.id,
            'doctor_id': self.doctor_id.id,
            'appointment_date': self.appointment_date
        }

        # create object for the model hospital.appointment and called the create method
        appointment_rec = self.env['hospital.appointment'].create(values)
        return {
            'name': _('Appointment'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'hospital.appointment',
            'res_id': appointment_rec.id,
            # 'target': 'new',
        }

    def action_view_appointment(self):
        # method 1
        # action = self.env.ref('om_hospital.action_hospital_appointment').read()[0]
        # action['domain'] = [('patient_id', '=', self.patient_id.id)]
        # method 2
        # We can use the action below as well it gives the same result
        # action = self.env['ir.actions.actions']._for_xml_id("om_hospital.action_hospital_appointment")
        # action['domain'] = [('patient_id', '=', self.patient_id.id)]
        # return action

        # method 3
        action = {
            'type': 'ir.actions.act_window',
            'name': 'Appointments',
            'res_model': 'hospital.appointment',
            'view_type': 'form',
            'domain': [('patient_id', '=', self.patient_id.id)],
            'view_mode': 'tree,form',
            'target': 'current',
        }
        return action

