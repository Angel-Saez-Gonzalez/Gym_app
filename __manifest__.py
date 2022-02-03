# -*- coding: utf-8 -*-
{
    'name': "gym_app",

    'summary': """
        Application to control the gym""",

    'description': """
        Application tan allows you to control alll the aspects of what a gym needs
    """,

    'author': "AssYuso(Angel) S.L.",
    'website': "http://www.assyuso.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/client_view.xml',
        'views/invoice_view.xml',
        'views/line_view.xml',
        'views/product_view.xml',
        'views/class_view.xml',
        'views/trainer_view.xml',
        'views/dailytask_view.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
}
