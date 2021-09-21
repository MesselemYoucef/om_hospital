# -*- coding: utf-8 -*-
{
    'name': 'Hospital Management',
    'version': '1.1',
    'summary': 'Hospital Management Software',
    'sequence': -100,
    'description': """Hospital Management Software""",
    'category': 'Productivity',
    'website': 'https://www.odoo.com',
    'Licence': 'LGPL-3',
    'images': [],
    'depends': [
        'sale',
        'mail',
        'report_xlsx'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'wizard/create_appointment_view.xml',
        'wizard/search_appointment_view.xml',
        'wizard/appointment_report.xml',
        'views/patient_view.xml',
        'views/kids_view.xml',
        'views/adults_view.xml',
        'views/patient_gender_view.xml',
        'views/appointment_views.xml',
        'views/sale.xml',
        'views/doctor_view.xml',
        'report/patient_card.xml',
        'report/report.xml',
        'report/appointment_details.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
