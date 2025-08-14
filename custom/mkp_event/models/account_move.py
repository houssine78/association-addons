from odoo import fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    is_mkp_event_invoice = fields.Boolean()
    mkp_event_budget_id = fields.Many2one("mkp.event.budget")
    expense_tag_id = fields.Many2one("mkp.event.budget.expense.config")
