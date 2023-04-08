# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Faculty',
    'version' : '1.0',
    'summary': 'Faculty information',
    'sequence': 15,
    'description': """ Faculty """,
    'category': 'Employees',
    'website': 'https://www.google.com',
    'images' : [],
    'depends': [
        'base',
        'website',
    ],
    'data': [
    # Security
        'security/ir.model.access.csv',
    # views
        'views/se_faculty_list.xml',
        'views/template.xml',

    ],
    'demo': [
    
    ],
    'qweb': [
    
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
