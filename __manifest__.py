# -*- coding: utf-8 -*-
{
    'name': "Sanergy",

    'summary': """
        Add, maintain and close FLT""",

    'description': """
        Add, maintain and close FLT
    """,

    'author': "Sanergy",
    'website': "https://www.saner.gy",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Technical',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'report/flt_report_templates.xml',
        'report/flt_report_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
