from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    mkp_product = fields.Boolean()
    product_event_type = fields.Selection([
        ('nwta_partipant', 'NWTA Participant'),
        ('nwta_staff', 'NWTA Staff'),
        ('wei', 'WEI'),
        ('st1', 'ST1'),
        ('guts', 'GUTS'),
        ('lt1', 'LT1'),
        ('lt2', 'LT2'),
        ('lt3', 'LT3'),
        ('grant', 'Grant')
        ]
    )
