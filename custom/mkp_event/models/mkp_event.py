from odoo import api, fields, models


class MKPEvent(models.Model):
    _name = "mkp.event"

    name = fields.Char(required=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    event_type = fields.Selection(
        [
            ("nwta", "NWTA"),
            ("wei", "WEI"),
            ("st1", "ST1"),
            ("guts", "GUTS"),
            ("lt1", "LT1"),
            ("lt2", "LT2"),
            ("lt3", "LT3"),
        ],
        required=True,
    )
    place = fields.Many2one(
        "res.partner", domain="[('is_initiation_place', '=', True)]", required=True
    )
    analytic_tag_ids = fields.Many2many("account.analytic.tag")
    participation_fee = fields.Monetary(
        required=True, currency_field="company_currency_id"
    )
    staff_fee = fields.Monetary(required=True, currency_field="company_currency_id")
    staff_product_id = fields.Many2one("product.product", required=True)
    participation_product_id = fields.Many2one("product.product", required=True)
    participation_max = fields.Integer()
    staff_max = fields.Integer()
    confirmed_participant = fields.Integer()
    confirmed_staff = fields.Integer()
    registered_participant = fields.Integer()
    registered_staff = fields.Integer()
    participant_subscription = fields.One2many(
        "mkp.event.subscription",
        "mkp_event_id",
        domain=[("subscription_type", "=", "participant")],
    )
    staff_subscription = fields.One2many(
        "mkp.event.subscription",
        "mkp_event_id",
        domain=[("subscription_type", "=", "staff")],
    )
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("confirmed", "Confirmed"),
            ("done", "Done"),
            ("cancelled", "Cancelled"),
        ],
        default="draft",
    )
    company_id = fields.Many2one(
        "res.company", required=True, index=True, default=lambda self: self.env.company
    )
    company_currency_id = fields.Many2one(
        string="Company Currency",
        related="company_id.currency_id",
        readonly=True,
    )
    event_coordinator = fields.Many2one("res.users", required=True)
    event_treasurer = fields.Many2one(
        "res.users",
    )
    participant_coordinator = fields.Many2one(
        "res.users",
    )
    staff_coordinator = fields.Many2one(
        "res.users",
    )
    pis_coordinator = fields.Many2one("res.users", string="PIS Coordinator")
    event_leader_ids = fields.Many2many("res.users", string="Event Leaders")
    event_leader_on_point = fields.Many2one(
        "res.users",
    )
    event_full_leader = fields.Many2one(
        "res.users",
    )

    @api.onchange("event_type")
    def _onchange_event_type(self):
        Product = self.env["product.product"]
        for event in self:
            if event.event_type == "nwta":
                nwta_products = Product.search(
                    [
                        ("mkp_product", "=", True),
                    ]
                )
                event.participation_product_id = nwta_products.filtered(
                    lambda product: product.product_event_type == "nwta_partipant"
                )[0]
                event.staff_product_id = nwta_products.filtered(
                    lambda product: product.product_event_type == "nwta_staff"
                )[0]

    @api.onchange("participation_product_id")
    def _onchange_participation_product_id(self):
        for event in self:
            event.participation_fee = event.participation_product_id.lst_price

    @api.onchange("staff_product_id")
    def _onchange_staff_product_id(self):
        for event in self:
            event.staff_fee = event.staff_product_id.lst_price
