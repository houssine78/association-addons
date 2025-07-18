# Copyright 2025 - Open Architects Consulting SRL
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "MKP Event",
    "version": "18.0.1.0.0",
    "category": "Event",
    "author": "Open Architects Consulting SRL, Houssine Bakkali",
    "license": "AGPL-3",
    "depends": ["base", "account", "product", "hr_expense"],
    "data": [
        "security/mkp_event_security.xml",
        "security/ir.model.access.csv",
        "data/mkp_event_budget_data.xml",
        "views/account_move_views.xml",
        "views/mkp_event_views.xml",
        "views/mkp_event_budget_views.xml",
        "views/mkp_event_budget_expense_config_views.xml",
        "views/mkp_event_subscription_views.xml",
        "views/hr_expense_sheet_views.xml",
        "views/product_views.xml",
        "views/res_partner_views.xml",
        "views/mkp_event_menuitem.xml",
        "views/res_users_views.xml",
    ],
    "installable": True,
}
