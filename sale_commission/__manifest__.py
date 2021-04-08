# Copyright 2014-2020 Tecnativa - Pedro M. Baeza
{
    'name': 'Sales commissions',
<<<<<<< HEAD
    'version': '12.0.1.4.0',
    'version': '12.0.3.1.0',
    'author': 'Tecnativa',
=======
    'version': '12.0.3.1.2',
    'author': 'Tecnativa,'
              'Odoo Community Association (OCA)',
>>>>>>> 163c4ec76e7df717ca9b05da8abae065f5c720e2
    'category': 'Sales Management',
    'license': 'AGPL-3',
    'depends': [
        'account',
        'product',
        'sale_management',
    ],
    'website': 'https://github.com/OCA/commission',
    'development_status': 'Mature',
    'maintainers': [
        'pedrobaeza',
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/sale_commission_security.xml',
        'views/sale_commission_view.xml',
        'views/sale_commission_mixin_views.xml',
        'views/product_template_view.xml',
        'views/res_partner_view.xml',
        'views/sale_order_view.xml',
        'views/account_invoice_view.xml',
        'views/sale_commission_settlement_view.xml',
        'views/sale_commission_settlement_report.xml',
        'views/report_settlement_templates.xml',
        'report/sale_commission_analysis_report_view.xml',
        'report/sale_order_commission_analysis_report_view.xml',
        'wizard/wizard_settle.xml',
        'wizard/wizard_invoice.xml',
    ],
    'demo': [
        'demo/sale_agent_demo.xml',
    ],
    'installable': True,
}
