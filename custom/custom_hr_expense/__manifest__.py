# Copyright 2025 Open Architects Consulting SRL
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Custom HR Expense",
    "version": "18.0.1.0.0",
    "category": "Human Resources",
    "author": "Open Architects Consulting SRL, Houssine Bakkali",
    "license": "AGPL-3",
    "depends": [
        "hr_expense",
        "hr_expense_analytic_tag"
    ],
    "data": [
        "views/hr_expense_view.xml",
    ],
    'installable': True,
    'auto_install': True,
}
