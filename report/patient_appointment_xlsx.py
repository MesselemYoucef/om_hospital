from odoo import models
import base64
import io


class PatientAppointmentXlsx(models.AbstractModel):
    _name = 'report.om_hospital.report_patient_appointment_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, patients):
        bold = workbook.add_format({'bold': True})
        format_align = workbook.add_format({'bold': True,
                                            'align': 'center',
                                            'bg_color': 'yellow'})

        sheet = workbook.add_worksheet('Appointments')
        sheet.set_column("D:D", 18)
        sheet.set_column("E:E", 25)
        row = 3
        col = 3
        sheet.write(row, col, 'Reference', bold)
        sheet.write(row, col + 1, 'Patient Name', bold)

        for appointment in data['appointments']:
            row += 1
            sheet.write(row, col, appointment['reference'])
            sheet.write(row, col + 1, appointment['patient_id'][1])
            print(appointment)
