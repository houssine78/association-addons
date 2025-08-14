from odoo import api, fields, models, _


class MKPEventBudget(models.Model):
    _name = "mkp.event.budget"

    name = fields.Char()
    mkp_event_id = fields.Many2one("mkp.event")
    event_type = fields.Selection(related="mkp_event_id.event_type")
    analytic_tag_ids = fields.Many2many(related="mkp_event_id.analytic_tag_ids")
    revenues_budgeted = fields.Monetary(
        compute="_compute_revenues_budgeted", currency_field="company_currency_id"
    )
    expenses_budgeted = fields.Monetary(
        compute="_compute_expenses_budgeted",
        currency_field="company_currency_id",
    )
    result_budgeted = fields.Monetary(
        compute="_compute_result_budgeted", currency_field="company_currency_id"
    )
    revenues_achieved = fields.Monetary(
        compute="_compute_revenues_achieved", currency_field="company_currency_id"
    )
    expenses_achieved = fields.Monetary(
        compute="_compute_total_expenses_achieved",
        currency_field="company_currency_id",
        store=True,
    )
    result_achieved = fields.Monetary(
        compute="_compute_result_achieved",
        currency_field="company_currency_id",
        store=True,
    )
    participation_fee = fields.Monetary(
        related="mkp_event_id.participation_fee", currency_field="company_currency_id"
    )
    participant_expected = fields.Integer()
    participant_achieved = fields.Integer()
    participant_revenues_budgeted = fields.Monetary(
        compute="_compute_participant_revenues_budgeted",
        currency_field="company_currency_id",
        store=True,
    )
    participant_revenues_achieved = fields.Monetary(
        compute="_compute_participant_revenues_achieved",
        currency_field="company_currency_id",
        store=True,
    )
    participant_grant_budgeted = fields.Monetary(currency_field="company_currency_id")
    participant_grant_achieved = fields.Monetary(
        compute="_compute_grant_achieved",
        currency_field="company_currency_id",
        store=True,
    )
    staff_fee = fields.Monetary(
        related="mkp_event_id.staff_fee", currency_field="company_currency_id"
    )
    staff_expected = fields.Integer()
    staff_achieved = fields.Integer()
    staff_revenues_budgeted = fields.Monetary(
        compute="_compute_staff_revenues_budgeted",
        currency_field="company_currency_id",
        store=True,
    )
    staff_revenues_achieved = fields.Monetary(
        compute="_compute_staff_revenues_achieved",
        currency_field="company_currency_id",
        store=True,
    )
    staff_grant_budgeted = fields.Monetary(currency_field="company_currency_id")
    staff_grant_achieved = fields.Monetary(
        compute="_compute_grant_achieved",
        currency_field="company_currency_id",
        store=True,
    )
    mkpi_contribution = fields.Monetary(currency_field="company_currency_id")
    mkpi_contribution_budgeted = fields.Monetary(
        compute="_compute_mkpi_contribution_budgeted",
        currency_field="company_currency_id",
        store=True,
    )
    mkpi_contribution_achieved = fields.Monetary(
        compute="_compute_mkpi_contribution_achieved",
        currency_field="company_currency_id",
        store=True,
    )
    co_leader_budgeted = fields.Integer()
    co_leader_achieved = fields.Integer()
    full_leader_budgeted = fields.Integer()
    full_leader_achieved = fields.Integer()
    co_leader_salary = fields.Monetary(
        default=500, currency_field="company_currency_id"
    )
    full_leader_salary = fields.Monetary(
        default=900, currency_field="company_currency_id"
    )
    fiscal_and_social_coeff = fields.Float(default=0.85)
    salary_budgeted = fields.Monetary(
        compute="_compute_salary_budgeted",
        currency_field="company_currency_id",
        store=True,
    )
    rent_budgeted = fields.Monetary(currency_field="company_currency_id")
    transportation_budgeted = fields.Monetary(currency_field="company_currency_id")
    prep_commitee_budgeted = fields.Monetary(currency_field="company_currency_id")
    participant_coord_budgeted = fields.Monetary(currency_field="company_currency_id")
    staff_coord_budgeted = fields.Monetary(currency_field="company_currency_id")
    pre_staff_budgeted = fields.Monetary(currency_field="company_currency_id")
    comeback_budgeted = fields.Monetary(currency_field="company_currency_id")
    pis_budgeted = fields.Monetary(currency_field="company_currency_id")
    ordinary_materials_budgeted = fields.Monetary(currency_field="company_currency_id")
    container_budgeted = fields.Monetary(currency_field="company_currency_id")
    sweat_budgeted = fields.Monetary(currency_field="company_currency_id")
    except_materials_budgeted = fields.Monetary(currency_field="company_currency_id")
    other_budgeted = fields.Monetary(currency_field="company_currency_id")
    salary_expense = fields.Monetary(
        compute="_compute_expenses_achieved",
        currency_field="company_currency_id",
        store=True,
    )
    rent_expense = fields.Monetary(
        compute="_compute_expenses_achieved",
        currency_field="company_currency_id",
        store=True,
    )
    transportation_expense = fields.Monetary(
        compute="_compute_expenses_achieved",
        currency_field="company_currency_id",
        store=True,
    )
    prep_commitee_expense = fields.Monetary(
        compute="_compute_expenses_achieved",
        currency_field="company_currency_id",
        store=True,
    )
    participant_coord_expense = fields.Monetary(
        compute="_compute_expenses_achieved",
        currency_field="company_currency_id",
        store=True,
    )
    staff_coord_expense = fields.Monetary(
        compute="_compute_expenses_achieved",
        currency_field="company_currency_id",
        store=True,
    )
    pre_staff_expense = fields.Monetary(
        compute="_compute_expenses_achieved",
        currency_field="company_currency_id",
        store=True,
    )
    comeback_expense = fields.Monetary(
        compute="_compute_expenses_achieved",
        currency_field="company_currency_id",
        store=True,
    )
    pis_expense = fields.Monetary(
        compute="_compute_expenses_achieved",
        currency_field="company_currency_id",
        store=True,
    )
    ordinary_materials_expense = fields.Monetary(
        compute="_compute_expenses_achieved",
        currency_field="company_currency_id",
        store=True,
    )
    container_expense = fields.Monetary(
        compute="_compute_expenses_achieved",
        currency_field="company_currency_id",
        store=True,
    )
    sweat_expense = fields.Monetary(
        compute="_compute_expenses_achieved",
        currency_field="company_currency_id",
        store=True,
    )
    except_materials_expense = fields.Monetary(
        compute="_compute_expenses_achieved",
        currency_field="company_currency_id",
        store=True,
    )
    other_expense = fields.Monetary(
        compute="_compute_expenses_achieved",
        currency_field="company_currency_id",
        store=True,
    )
    nb_expense = fields.Integer(
        compute="_compute_nb_expense", string="Number of Expenses"
    )
    nb_account_move = fields.Integer(
        string="Number of Journal Entries", compute="_compute_nb_account_move"
    )
    hr_expense_sheet_ids = fields.One2many(
        "hr.expense.sheet",
        "mkp_event_budget_id",
        domain=[
            ("is_mkp_event_expense", "=", True),
        ],
    )
    account_move_ids = fields.One2many(
        "account.move",
        "mkp_event_budget_id",
        domain=[
            ("is_mkp_event_invoice", "=", True),
            ("move_type", "in", ["in_invoice", "in_refund"]),
        ],
    )
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("confirmed", "Confirmed"),
            ("closed", "Closed"),
            ("cancelled", "Cancelled"),
        ],
        default="draft",
    )
    company_currency_id = fields.Many2one(
        string="Company Currency",
        related="mkp_event_id.company_currency_id",
        readonly=True,
    )

    @api.depends("hr_expense_sheet_ids.expense_line_ids")
    def _compute_nb_expense(self):
        for budget in self:
            budget.nb_expense = len(budget.hr_expense_sheet_ids.expense_line_ids)

    @api.depends("account_move_ids")
    def _compute_nb_account_move(self):
        for budget in self:
            budget.nb_account_move = len(budget.account_move_ids)

    @api.onchange("mkp_event_id")
    def _onchange_mkp_event_id(self):
        for budget in self:
            if budget.mkp_event_id:
                budget.name = "Budget " + budget.mkp_event_id.name

    def _compute_revenues_budgeted(self):
        for budget in self:
            budget.revenues_budgeted = (
                budget.participant_revenues_budgeted + budget.staff_revenues_budgeted
            )

    def _compute_expenses_budgeted(self):
        for budget in self:
            budget.expenses_budgeted = 0.0

    def _compute_result_budgeted(self):
        for budget in self:
            budget.result_budgeted = budget.revenues_budgeted - budget.expenses_budgeted

    def _compute_revenues_achieved(self):
        for budget in self:
            budget.revenues_achieved = (
                budget.participant_revenues_achieved + budget.staff_revenues_achieved
            )

    @api.depends(
        "account_move_ids.state",
        "account_move_ids.is_mkp_event_invoice",
        "account_move_ids.expense_tag_id",
        "account_move_ids.expense_tag_id.expense_category",
        "account_move_ids.amount_total",
        "hr_expense_sheet_ids.state",
        "hr_expense_sheet_ids.is_mkp_event_expense",
        "hr_expense_sheet_ids.expense_line_ids",
        "hr_expense_sheet_ids.expense_line_ids.state",
        "hr_expense_sheet_ids.expense_line_ids.total_amount",
        "hr_expense_sheet_ids.expense_line_ids.expense_tag_id",
        "hr_expense_sheet_ids.expense_line_ids.expense_tag_id.expense_category",
    )
    def _compute_expenses_achieved(self):
        ExpenseTagList = self.env["mkp.event.budget.expense.config"]
        exp_tag_list = ExpenseTagList.search([]).mapped("expense_category")
        for budget in self:
            expenses_achieved = {exp_tag: 0.0 for exp_tag in exp_tag_list}

            invoices = budget.account_move_ids.filtered(
                lambda inv: inv.is_mkp_event_invoice
                and inv.state in ["draft", "posted"]
                and inv.expense_tag_id
            )
            expense_sheets = budget.hr_expense_sheet_ids.filtered(
                lambda sheet: sheet.is_mkp_event_expense and sheet.state != "cancel"
            )

            for invoice in invoices:
                expense_tag = invoice.expense_tag_id.expense_category
                expenses_achieved[expense_tag] += invoice.amount_total

            for expense_sheet in expense_sheets:
                lines = expense_sheet.expense_line_ids.filtered(
                    lambda line: line.expense_tag_id and line.state != "refused"
                )
                for line in lines:
                    expense_tag = line.expense_tag_id.expense_category
                    expenses_achieved[expense_tag] += line.total_amount

            for key, amount in expenses_achieved.items():
                if hasattr(budget, f"{key}_expense"):
                    setattr(budget, f"{key}_expense", amount)

    @api.depends(
        "revenues_achieved",
        "expenses_achieved",
    )
    def _compute_result_achieved(self):
        for budget in self:
            budget.result_achieved = budget.revenues_achieved - budget.expenses_achieved

    @api.depends(
        "salary_expense",
        "rent_expense",
        "transportation_expense",
        "prep_commitee_expense",
        "participant_coord_expense",
        "staff_coord_expense",
        "pre_staff_expense",
        "comeback_expense",
        "pis_expense",
        "ordinary_materials_expense",
        "container_expense",
        "sweat_expense",
        "except_materials_expense",
        "other_expense",
        "mkpi_contribution_achieved",
    )
    def _compute_total_expenses_achieved(self):
        for budget in self:
            budget.expenses_achieved = (
                budget.salary_expense
                + budget.rent_expense
                + budget.transportation_expense
                + budget.prep_commitee_expense
                + budget.participant_coord_expense
                + budget.staff_coord_expense
                + budget.pre_staff_expense
                + budget.comeback_expense
                + budget.pis_expense
                + budget.ordinary_materials_expense
                + budget.container_expense
                + budget.sweat_expense
                + budget.except_materials_expense
                + budget.other_expense
                + budget.mkpi_contribution_achieved
            )

    @api.depends(
        "participation_fee", "participant_expected", "participant_grant_budgeted"
    )
    def _compute_participant_revenues_budgeted(self):
        for budget in self:
            budget.participant_revenues_budgeted = (
                budget.participation_fee * budget.participant_expected
                - budget.participant_grant_budgeted
            )

    @api.depends(
        "participation_fee", "participant_achieved", "participant_grant_achieved"
    )
    def _compute_participant_revenues_achieved(self):
        for budget in self:
            budget.participant_revenues_achieved = (
                budget.participation_fee * budget.participant_achieved
                - budget.participant_grant_achieved
            )

    @api.depends("staff_fee", "staff_expected", "staff_grant_budgeted")
    def _compute_staff_revenues_budgeted(self):
        for budget in self:
            budget.staff_revenues_budgeted = (
                budget.staff_fee * budget.staff_expected - budget.staff_grant_budgeted
            )

    @api.depends("staff_fee", "staff_achieved", "staff_grant_achieved")
    def _compute_staff_revenues_achieved(self):
        for budget in self:
            budget.staff_revenues_achieved = (
                budget.staff_fee * budget.staff_achieved - budget.staff_grant_achieved
            )

    @api.depends(
        "mkp_event_id",
        "mkp_event_id.staff_subscription",
        "mkp_event_id.staff_subscription.grant",
        "mkp_event_id.staff_subscription.state",
        "mkp_event_id.staff_subscription.grant_amount",
        "mkp_event_id.participant_subscription",
        "mkp_event_id.participant_subscription.grant",
        "mkp_event_id.participant_subscription.state",
        "mkp_event_id.participant_subscription.grant_amount",
    )
    def _compute_grant_achieved(self):
        for budget in self:
            mkp_event = budget.mkp_event_id

            grant_staff_subs = mkp_event.staff_subscription.filtered(
                lambda sub: sub.grant and sub.state == "registered"
            )
            part_staff_subs = mkp_event.participant_subscription.filtered(
                lambda sub: sub.grant and sub.state == "registered"
            )

            grant_staff_amount = 0
            grant_part_amount = 0

            for grant_staff_sub in grant_staff_subs:
                grant_staff_amount += grant_staff_sub.grant_amount

            for part_staff_sub in part_staff_subs:
                grant_part_amount += part_staff_sub.grant_amount

            budget.staff_grant_achieved = grant_staff_amount
            budget.participant_grant_achieved = grant_part_amount

    @api.depends(
        "fiscal_and_social_coeff",
        "co_leader_salary",
        "co_leader_budgeted",
        "full_leader_salary",
        "full_leader_budgeted",
    )
    def _compute_salary_budgeted(self):
        for budget in self:
            budget.salary_budgeted = (
                budget.co_leader_salary
                * budget.co_leader_budgeted
                * (1 + budget.fiscal_and_social_coeff)
            ) + (
                budget.full_leader_salary
                * budget.full_leader_budgeted
                * (1 + budget.fiscal_and_social_coeff)
            )

    @api.depends(
        "mkpi_contribution",
        "participant_expected",
    )
    def _compute_mkpi_contribution_budgeted(self):
        for budget in self:
            budget.mkpi_contribution_budgeted = (
                budget.mkpi_contribution * budget.participant_expected
            )

    @api.depends(
        "mkpi_contribution",
        "participant_achieved",
    )
    def _compute_mkpi_contribution_achieved(self):
        for budget in self:
            budget.mkpi_contribution_achieved = (
                budget.mkpi_contribution * budget.participant_achieved
            )

    def action_open_expense_view(self):
        self.ensure_one()
        if self.nb_expense == 1:
            return {
                "type": "ir.actions.act_window",
                "view_mode": "form",
                "res_model": "hr.expense",
                "res_id": self.expense_line_ids.id,
            }
        return {
            "name": _("Expenses"),
            "type": "ir.actions.act_window",
            "view_mode": "list,form",
            "views": [[False, "list"], [False, "form"]],
            "res_model": "hr.expense",
            "domain": [("id", "in", self.hr_expense_sheet_ids.expense_line_ids.ids)],
        }

    def action_open_account_moves(self):
        self.ensure_one()
        action = {
            "name": _("Event Bills"),
            "type": "ir.actions.act_window",
            "res_model": "account.move",
            "context": {
                "default_move_type": "in_invoice",
                "default_is_mkp_event_invoice": True,
                "default_mkp_event_budget_id": self.id,
            },
        }
        if len(self.account_move_ids) == 1:
            action.update(
                {
                    "view_mode": "form",
                    "res_id": self.account_move_ids.id,
                    "views": [(False, "form")],
                }
            )
        else:
            action.update(
                {
                    "view_mode": "list",
                    "domain": [("id", "in", self.account_move_ids.ids)],
                    "views": [(False, "list"), (False, "form")],
                }
            )
        return action
