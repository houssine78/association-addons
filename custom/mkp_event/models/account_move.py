from odoo import fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    is_mkp_event_invoice = fields.Boolean()
