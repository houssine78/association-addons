from odoo import fields, models


class HrExpense(models.Model):
    _inherit = "hr.expense"

    is_mkp_event_expense = fields.Boolean(related="sheet_id.is_mkp_event_expense")
    mkp_event_budget_id = fields.Many2one(related="sheet_id.mkp_event_budget_id")
    expense_tag_id = fields.Many2one("mkp.event.budget.expense.config")
