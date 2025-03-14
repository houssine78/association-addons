from odoo import api,Command, models, fields

class SetAnalyticTagWizard(models.TransientModel):
    _name = 'set.analytic.tag.wizard'
    _description = 'Set analytic tag on account.move.line'

    def _default_account_move_ids(self):
        account_move_ids = self.env.context.get('active_ids', [])
        account_moves = self.env['account.move'].sudo().browse(account_move_ids)

        return [Command.link(account_move.id) for account_move in account_moves]

    account_move_ids = fields.Many2many(
        comodel_name="account.move",
        string="Invoices",
        default=_default_account_move_ids
    )
    account_analytic_tag = fields.Many2one(
        comodel_name="account.analytic.tag",
        string="Analytic tag"
    )

    def set_analytic_tag(self):
        for account_move in self.account_move_ids:
            if account_move.state == "posted" :
                account_move.button_draft()
            for line in account_move.invoice_line_ids:
                line.analytic_tag_ids = [self.account_analytic_tag.id]
            account_move.action_post()
                
        return True
