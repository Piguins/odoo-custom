{
    'name': "Hello World",
    'summary': "A simple Hello World module for Odoo 17",
    'description': """
        This module displays a Hello World message in Odoo.
    """,
    'author': "Trần Ngọc Huyền Trang",
    'version': '1.0',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',  # Thêm dòng này
        'views/hello_world_views.xml',
    ],
    'installable': True,
    'application': True,
}