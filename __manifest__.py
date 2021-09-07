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
    #'images': [
    #    'static/img/default_image.png',
    #],
    # any module necessary for this one to work correctly
    'depends': ['base','hr','mail'],

    # always loaded
    'data': [
        'security/flt_security.xml',
        'security/ir.model.access.csv',
        'wizard/update_status.xml',
        'views/views.xml',
        'views/templates.xml',
        'report/flt_report_templates.xml',
        'report/flt_report_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
