# Copyright 2023 Tecnativa - Víctor Martínez
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
from odoo import fields, models


class HrExpense(models.Model):
    _inherit = "hr.expense"

    analytic_tag_ids = fields.Many2many(
        comodel_name="account.analytic.tag",
        string="Analytic Tags",
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",
    )

    def _prepare_move_lines_vals(self):
        vals = super()._prepare_move_lines_vals()
        if self.analytic_tag_ids:
            vals.update({"analytic_tag_ids": [(6, 0, self.analytic_tag_ids.ids)]})
        if self.analytic_distribution:
            vals.update({"analytic_distribution": self.analytic_distribution})
        return vals

