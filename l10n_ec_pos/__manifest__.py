# -*- coding: utf-8 -*-
{
    'name': 'Ecuador - Point of Sale',
    'version': '17.0.1.0.0',
    'summary': """Localización ecuatoriana para Punto de Venta""",
    'author': 'Danilo Sanchez',
    'website': '',
    'category': 'Accounting/Localizations/Point of Sale',
    'depends': ['point_of_sale', 'l10n_ec_account_edi'],
    'data': [
        'views/pos_config_views.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'l10n_ec_pos/static/src/**/*',
        ],
    },
    'application': False,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
