from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.users"

    is_leader = fields.Boolean(related="partner_id.is_leader")
    leadership = fields.Selection(related="partner_id.leadership")
    staff_count = fields.Integer(related="partner_id.staff_count")
