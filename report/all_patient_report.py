from odoo import api, models, fields


class AllPatientReport(models.AbstractModel):
    _name = "report.om_hospital.report_all_patient_list"
    _description = "Patients Report"

    @api.model
    def _get_report_values(self, docids, data=None):
        """Generates the report for the patient according to Age and Gender selection"""
        domain = []
        gender = data.get('form_data').get('gender')
        age = data.get('form_data').get('age')
        if gender:
            domain.append(('gender', '=', gender))
        if age != 0:
            domain.append(('age', '=', age))
        docs = self.env['hospital.patient'].search(domain)
        return {
            'docs': docs,
        }


class PatientDetailsReport(models.AbstractModel):
    _name = "report.om_hospital.report_patient_card"
    _description = "Patient Details"

    @api.model
    def _get_report_values(self, docids, data=None):
        print("------------------>", docids)
        docs = self.env['hospital.patient'].browse(docids)
        return {
            'docs': docs
        }