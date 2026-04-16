from odoo import Command, _, fields, models
from odoo.exceptions import UserError


class SetAnalyticTagWizard(models.TransientModel):
    _name = 'set.analytic.tag.wizard'
    _inherit = ['analytic.mixin']
    _description = 'Set analytic tag and/or analytic distribution on account.move.line'

    def _default_account_move_ids(self):
        account_move_ids = self.env.context.get('active_ids', [])
        acc_moves = self.env['account.move'].sudo().browse(account_move_ids)

        return [Command.link(account_move.id) for account_move in acc_moves]

    account_move_ids = fields.Many2many(
        comodel_name="account.move",
        string="Invoices",
        default=_default_account_move_ids,
    )
    account_analytic_tag = fields.Many2one(
        comodel_name="account.analytic.tag",
        string="Analytic tag",
    )
    company_id = fields.Many2one(
        comodel_name="res.company",
        default=lambda self: self.env.company,
        required=True,
    )
    # analytic_distribution is provided by analytic.mixin

    def set_analytic_tag(self):
        self.ensure_one()
        if not self.account_analytic_tag and not self.analytic_distribution:
            raise UserError(_(
                "Please provide at least an analytic tag or an analytic "
                "distribution."
            ))

        for account_move in self.account_move_ids:
            reset_to_draft = account_move.state == "posted"
            if reset_to_draft:
                account_move.button_draft()

            line_vals = {}
            if self.account_analytic_tag:
                line_vals['analytic_tag_ids'] = [
                    Command.set([self.account_analytic_tag.id])
                ]
            if self.analytic_distribution:
                line_vals['analytic_distribution'] = self.analytic_distribution

            if line_vals:
                account_move.invoice_line_ids.write(line_vals)

            if reset_to_draft:
                account_move.action_post()

        return True
