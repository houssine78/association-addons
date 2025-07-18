from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    is_initiation_place = fields.Boolean()
    is_leader = fields.Boolean()
    leadership = fields.Selection([
            ("lit", "LIT"),
            ("clc", "CLC"),
            ("co-leader", "Co-Leader"),
            ("full", "Full Leader"),
        ],
    )
    staff_count = fields.Integer(string="Number of staff")
