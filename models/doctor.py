from odoo import api, fields, models, _


class Doctor(models.Model):
    _name = "hospital.doctor"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Doctor"
    # You define a rec name when you don't have the "name" attribute in the model
    _rec_name = "doctor_name"

    doctor_name = fields.Char(string="Name", required=True, tracking=True)
    age = fields.Integer(string="Age", tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], required=True, default="male", tracking=True)
    note = fields.Text(string="Description")
    image = fields.Binary(string="Patient Image")
