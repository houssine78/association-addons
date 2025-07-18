from odoo import fields, models


class HrExpenseSheet(models.Model):
    _inherit = "hr.expense.sheet"

    is_mkp_event_expense = fields.Boolean()
    mkp_event_budget_id = fields.Many2one("mkp.event.budget")
