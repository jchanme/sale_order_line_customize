# -*- coding: utf-8 -*-
{
    'name': "Sale Order Line Customize",
    'summary': """
        Adds custom fields to Sale Order Lines""",
    'description': """
        This Module Adds Custom Fields to order Lines in Sales orders and in Purchase orders Dynamically After the Products added and Saved.
    """,
    'author': "Safyric Co., Ltd.",
    'website': "https://www.safyric.com",
    'category': 'Business',
    'version': '0.5',
    'depends': ['base', 'sale', 'purchase'],
    'data': [
        'views/sale_order_line_template.xml',
        'views/purchase_order_line_template.xml',
    ],
}
