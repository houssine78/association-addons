from odoo import api, fields, models


class MKPEventSubscription(models.Model):
    _name = "mkp.event.subscription"

    mkp_event_id = fields.Many2one("mkp.event")
    partner_id = fields.Many2one("res.partner", required=True)
    subscription_type = fields.Selection([
            ("participant", "Participant"),
            ("staff", "Staff")
        ],
        required=True
    )
    product_id = fields.Many2one(
        "product.product",
        required=True
    )
    grant = fields.Boolean()
    subscription_amount = fields.Monetary(currency_field="company_currency_id")
    grant_amount = fields.Monetary(currency_field="company_currency_id")
    amount_due = fields.Monetary(
        compute="_compute_amount_due",
        currency_field="company_currency_id"
    )
    state = fields.Selection([
            ("draft", "Draft"),
            ("registered", "Registered"),
            ("waiting", "Waiting list"),
            ("reported", "Reported"),
            ("cancelled", "Cancelled")
        ],
        default="draft"
    )
    company_currency_id = fields.Many2one(
        string='Company Currency',
        related='mkp_event_id.company_currency_id',
        readonly=True,
    )
    invoice_id = fields.Many2one("account.move")

    @api.depends("grant", "subscription_amount", "grant_amount")
    def _compute_amount_due(self):
        for subscription in self:
            # TODO HBA return error when amount_due is negative
            if subscription.grant:
                subscription.amount_due = (
                    subscription.subscription_amount
                    - subscription.grant_amount
                )
            else:
                subscription.amount_due = subscription.subscription_amount

    @api.onchange('subscription_type')
    def _onchange_subscription_type(self):
        for subscription in self:
            mkp_event = subscription.mkp_event_id
            if mkp_event:
                if subscription.subscription_type == "participant":
                    product_id = mkp_event.participation_product_id
                elif subscription.subscription_type == "staff":
                    product_id = mkp_event.staff_product_id

                subscription.product_id = product_id

    @api.onchange('product_id')
    def _onchange_product_id(self):
        for subscription in self:
            product = subscription.product_id
            if product:
                subscription.subscription_amount = product.lst_price

    @api.onchange('grant')
    def _onchange_grant(self):
        for subscription in self:
            if not subscription.grant:
                subscription.grant_amount = 0.0

    # action button
    # TODO HBA create invoice
