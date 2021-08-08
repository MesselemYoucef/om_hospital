from odoo import models
import base64
import io


class PatientCardXlsx(models.AbstractModel):
    _name = 'report.om_hospital.report_patient_card_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, patients):
        bold = workbook.add_format({'bold': True})
        format_align = workbook.add_format({'bold': True,
                                            'align': 'center',
                                            'bg_color': 'yellow'})

        for obj in patients:
            row = 3
            col = 3
            sheet = workbook.add_worksheet(obj.name)
            sheet.set_column("D:D", 12)
            sheet.set_column("E:E", 13)
            sheet.merge_range(row, col, row, col+1, 'ID CARD', format_align)
            row += 1
            if obj.image:
                patient_image = io.BytesIO(base64.b64decode(obj.image))
                sheet.insert_image(row, col, "staff.png", {'image_data': patient_image, 'x_scale': 0.5, 'y_scale': 0.5})
                row += 7
            # One sheet by patient
            sheet.write(row, col, "Name", bold)
            sheet.write(row, col+1, obj.name)
            row += 1
            sheet.write(row, col, "Age", bold)
            sheet.write(row, col+1, obj.age)
            row += 1
            sheet.write(row, col, "Reference", bold)
            sheet.write(row, col+1, obj.reference)
            row += 2
