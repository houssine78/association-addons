# from odoo import fields, models
#
#
# class MKPEventLeader(models.Model):
#     _name = "mkp.event.leader"
#
#     mkp_event_id = fields.Many2one("mkp.event")
#     leader = fields.Many2one("res.users", required=True)
#     leader_type = fields.Selection([
#             ("on_point", "Leader on Point"),
#             ("full", "Full Leader"),
#             ("co-leader", "Co-Leader"),
#         ],
#         required=True
#     )
