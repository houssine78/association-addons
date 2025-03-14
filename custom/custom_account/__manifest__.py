# Copyright 2025 Open Architects Consulting SRL
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Custom account",
    "summary": "customisation for accounting",
    "version": "18.0.1.0.0",
    "category": "Account",
    "author": "Open Architects Consulting SRL, Houssine Bakkali",
    "license": "AGPL-3",
    "depends": [
        "account",
        "account_statement_base",
        "account_usability"
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/bank_statement_line.xml",
        "wizard/set_analytic_tag_wizard.xml"
    ],
    "installable": True,
}
