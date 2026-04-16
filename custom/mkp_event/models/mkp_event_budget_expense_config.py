from odoo import fields, models


class MKPEventBudgetExpenseConfig(models.Model):
    _name = "mkp.event.budget.expense.config"
    _description = "MKP Event Budget Expense Config"

    name = fields.Char(required=True)
    expense_category = fields.Selection(
        [
            ("salary", "Salary"),
            ("rent", "Rent"),
            ("transportation", "Transportation"),
            ("prep_commitee", "Preparation committee"),
            ("participant_coord", "Participant coordination"),
            ("staff_coord", "Staff coordination"),
            ("pre_staff", "Pre-staff"),
            ("comeback", "Come-back evening"),
            ("pis", "PIS"),
            ("ordinary_materials", "Ordinary materials"),
            ("container", "Container"),
            ("sweat", "Sweat"),
            ("except_materials", "Exceptional materials"),
            ("other", "Other"),
        ],
        required=True,
    )
    distribution_analytic_account_id = fields.Many2many("account.analytic.account")
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("active", "Active"),
            ("cancelled", "Cancelled"),
        ],
        default="draft",
    )
    # TODO add unicity constraint on expense_category and
    # distribution_analytic_account_id
