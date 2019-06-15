# -*- coding: utf-8 -*-
{
    'name': "l10n_ma_fix",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['l10n_ma'],
    'autoinstall': True,

    'data': [
        'data/account_tax_data.xml',
        'data/l10n_ma_chart_data.xml',
        'data/res_country_data.xml',
        'views/report_invoice.xml',
    ],
}