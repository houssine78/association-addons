from odoo import api, fields, models


class MKPEventBudget(models.Model):
    _name = "mkp.event.budget"

    name = fields.Char()
    mkp_event_id = fields.Many2one("mkp.event")
    event_type = fields.Selection(related="mkp_event_id.event_type")
    analytic_tag_ids = fields.Many2many(
        related="mkp_event_id.analytic_tag_ids"
    )
    revenues_budgeted = fields.Monetary(
        compute="_compute_revenues_budgeted",
        currency_field="company_currency_id"
    )
    expenses_budgeted = fields.Monetary(
        compute="_compute_expenses_budgeted",
        currency_field="company_currency_id",
    )
    result_budgeted = fields.Monetary(
        compute="_compute_result_budgeted",
        currency_field="company_currency_id"
    )
    revenues_achieved = fields.Monetary(
        compute="_compute_revenues_achieved",
        currency_field="company_currency_id"
    )
    expenses_achieved = fields.Monetary(
        compute="_compute_expenses_achieved",
        currency_field="company_currency_id",
    )
    result_achieved = fields.Monetary(
        compute="_compute_result_achieved",
        currency_field="company_currency_id"
    )
    participation_fee = fields.Monetary(
        related="mkp_event_id.participation_fee",
        currency_field="company_currency_id"
    )
    participant_expected = fields.Integer()
    participant_achieved = fields.Integer()
    participant_revenues_budgeted = fields.Monetary(
        compute="_compute_participant_revenues_budgeted",
        currency_field="company_currency_id"
    )
    participant_revenues_achieved = fields.Monetary(
        compute="_compute_participant_revenues_achieved",
        currency_field="company_currency_id"
    )
    participant_grant_budgeted = fields.Monetary(
        currency_field="company_currency_id"
    )
    participant_grant_achieved = fields.Monetary(
        currency_field="company_currency_id"
    )
    staff_fee = fields.Monetary(
        related="mkp_event_id.staff_fee",
        currency_field="company_currency_id"
    )
    staff_expected = fields.Integer()
    staff_achieved = fields.Integer()
    staff_revenues_budgeted = fields.Monetary(
        compute="_compute_staff_revenues_budgeted",
        currency_field="company_currency_id"
    )
    staff_revenues_achieved = fields.Monetary(
        compute="_compute_staff_revenues_achieved",
        currency_field="company_currency_id"
    )
    staff_grant_budgeted = fields.Monetary(
        currency_field="company_currency_id"
    )
    staff_grant_achieved = fields.Monetary(
        currency_field="company_currency_id"
    )
    mkpi_contribution = fields.Monetary(currency_field="company_currency_id")
    mkpi_contribution_budgeted = fields.Monetary(
        compute="_compute_mkpi_contribution_budgeted",
        currency_field="company_currency_id"
    )
    mkpi_contribution_achieved = fields.Monetary(
        compute="_compute_mkpi_contribution_achieved",
        currency_field="company_currency_id"
    )
    co_leader_budgeted = fields.Integer()
    co_leader_achieved = fields.Integer()
    full_leader_budgeted = fields.Integer()
    full_leader_achieved = fields.Integer()
    co_leader_salary = fields.Monetary(
        default=500,
        currency_field="company_currency_id"
    )
    full_leader_salary = fields.Monetary(
        default=900,
        currency_field="company_currency_id"
    )
    fiscal_and_social_coeff = fields.Float(default=0.85)
    salary_budgeted = fields.Monetary(
        compute="_compute_salary_budgeted",
        currency_field="company_currency_id"
    )
    salary_achieved = fields.Monetary(
        compute="_compute_salary_achieved",
        currency_field="company_currency_id"
    )
    hr_expense_sheet_ids = fields.One2many(
        "hr.expense.sheet",
        "mkp_event_budget_id"
    )
    state = fields.Selection([
            ("draft", "Draft"),
            ("confirmed", "Confirmed"),
            ("closed", "Closed"),
            ("cancelled", "Cancelled")
        ],
        default="draft"
    )
    company_currency_id = fields.Many2one(
        string='Company Currency',
        related='mkp_event_id.company_currency_id',
        readonly=True,
    )

    @api.onchange("mkp_event_id")
    def _onchange_mkp_event_id(self):
        for budget in self:
            if budget.mkp_event_id:
                budget.name = "Budget " + budget.mkp_event_id.name

    def _compute_revenues_budgeted(self):
        for budget in self:
            budget.revenues_budgeted = (
                budget.participant_revenues_budgeted
                + budget.staff_revenues_budgeted
            )

    def _compute_expenses_budgeted(self):
        for budget in self:
            budget.expenses_budgeted = 0.0

    def _compute_result_budgeted(self):
        for budget in self:
            budget.result_budgeted = (
                budget.revenues_budgeted - budget.expenses_budgeted
            )

    def _compute_revenues_achieved(self):
        for budget in self:
            budget.revenues_achieved = (
                budget.participant_revenues_achieved
                + budget.staff_revenues_achieved
            )

    def _compute_expenses_achieved(self):
        for budget in self:
            budget.expenses_achieved = 0.0

    def _compute_result_achieved(self):
        for budget in self:
            budget.result_achieved = (
                budget.revenues_achieved - budget.expenses_achieved
            )

    @api.depends(
        "participation_fee",
        "participant_expected",
        "participant_grant_budgeted"
    )
    def _compute_participant_revenues_budgeted(self):
        for event in self:
            event.participant_revenues_budgeted = (
                event.participation_fee * event.participant_expected
                - event.participant_grant_budgeted
            )

    @api.depends(
        "participation_fee",
        "participant_achieved",
        "participant_grant_achieved"
    )
    def _compute_participant_revenues_achieved(self):
        for event in self:
            event.participant_revenues_achieved = (
                event.participation_fee * event.participant_achieved
                - event.participant_grant_achieved
            )

    @api.depends("staff_fee", "staff_expected", "staff_grant_budgeted")
    def _compute_staff_revenues_budgeted(self):
        for event in self:
            event.staff_revenues_budgeted = (
                event.staff_fee * event.staff_expected
                - event.staff_grant_budgeted
            )

    @api.depends("staff_fee", "staff_achieved", "staff_grant_achieved")
    def _compute_staff_revenues_achieved(self):
        for event in self:
            event.staff_revenues_achieved = (
                event.staff_fee * event.staff_achieved
                - event.staff_grant_achieved
            )

    @api.depends(
        "fiscal_and_social_coeff",
        "co_leader_salary",
        "co_leader_budgeted",
        "full_leader_salary",
        "full_leader_budgeted",
    )
    def _compute_salary_budgeted(self):
        for event in self:
            event.salary_budgeted = (
                (event.co_leader_salary * event.co_leader_budgeted
                 * (1 + event.fiscal_and_social_coeff))
                +
                (event.full_leader_salary * event.full_leader_budgeted
                 * (1 + event.fiscal_and_social_coeff))
            )

    @api.depends(
        "fiscal_and_social_coeff",
        "co_leader_salary",
        "co_leader_achieved",
        "full_leader_salary",
        "full_leader_achieved",
    )
    def _compute_salary_achieved(self):
        for event in self:
            event.salary_achieved = (
                (event.co_leader_salary * event.co_leader_achieved
                 * (1 + event.fiscal_and_social_coeff))
                +
                (event.full_leader_salary * event.full_leader_achieved
                 * (1 + event.fiscal_and_social_coeff))
            )

    @api.depends(
        "mkpi_contribution",
        "participant_expected",
    )
    def _compute_mkpi_contribution_budgeted(self):
        for event in self:
            event.mkpi_contribution_budgeted = (
                event.mkpi_contribution * event.participant_expected
            )

    @api.depends(
        "mkpi_contribution",
        "participant_achieved",
    )
    def _compute_mkpi_contribution_achieved(self):
        for event in self:
            event.mkpi_contribution_achieved = (
                event.mkpi_contribution * event.participant_achieved
            )
