from odoo import models

class PatientCardXlsx(models.AbstractModel):
    _name = 'report.om_hospital.report_patient_card_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, patients):

        sheet = workbook.add_worksheet('PATIENT ID CARD')
        bold = workbook.add_format({'bold': True})
        row = 3
        col = 3
        sheet.set_column("D:E", 30)
        for obj in patients:
            row += 1
            # One sheet by patient
            sheet.write(row, col, "Name", bold)
            sheet.write(row, col+1, obj.name)
            row += 1
            sheet.write(row, col, "Age", bold)
            sheet.write(row, col+1, obj.age)
            row += 1
            sheet.write(row, col, "Reference", bold)
            sheet.write(row, col+1, obj.reference)
