{
    'name': 'AM Trip',
    'version': '10.0',
    'category': 'Customer',
    'sequence': 999,
    'summary': 'AM TRIP',
    'description': "",
    'depends': ['base', 'mt_config', 'account', 'mt_customer'],
    'data': [
        'data/accounting_data.xml',
        'data/am_group.xml',
        'data/company_data.xml',
        'views/trip_view.xml',
        'views/invoice_view.xml',
        'views/expense_view.xml',
        'report/trip_report.xml',
        'report/remaining_payments.xml',
        'report/report.xml',
        'security/ir.model.access.csv',
        
    ],
    'demo': [
        
    ],
    'installable': True,
    'application': True,
    'qweb': [''],
    'website': '',
}
