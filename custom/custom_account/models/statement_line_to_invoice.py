from odoo import fields, models


class StatementLineToInvoice(models.Model):
    _name = 'statement.line.to.invoice'
    _description = 'Transition model to track invoice creation from statement'

    email = fields.Char(
        required=True
    )
    name = fields.Char()
    partner_id = fields.Many2one(
        "res.partner",
        required=True
    )
    invoice_date = fields.Date()
    product_id = fields.Many2one(
        "product.product",
        required=True
    )
    currency_id = fields.Many2one(
        comodel_name='res.currency',
        related='bank_statement_line_id.currency_id',
    )
    amount = fields.Monetary()
    grant = fields.Boolean()
    grant_product = fields.Many2one(
        "product.product"
    )
    bank_statement_line_id = fields.Many2one(
        "account.bank.statement.line",
        string="Statement line",
        required = True
    )
    account_analytic_tag_id = fields.Many2one(
        "account.analytic.tag",
        string="Analytic tag"
    )
    invoice_id = fields.Many2one(
        "account.move",
    )
    state = fields.Selection([
        ('draft', 'Draft'),
        ('invoiced', 'Invoice'),
        ('error', 'error')],
        required = True
    )
    error_msg = fields.Char(string="Error message")

    def action_create_invoice(self):
        self.ensure_one()
        accountMove = self.env['account.move']
        moveLine = self.env['account.move.line']

        move_vals = {
            "move_type": "out_invoice",
            "invoice_date": self.invoice_date,
            "partner_id": self.partner_id.id
        }

        move = accountMove.create(move_vals)
        line_vals = {
            "move_id": move.id,
            "product_id": self.product_id.id,
            "analytic_tag_ids": [self.account_analytic_tag_id.id],
        }

        if self.amount > self.product_id.lst_price:
            line_vals['price_unit'] = self.amount

        line = moveLine.create(line_vals)    
        self.write({"state": "invoiced", "invoice_id": move.id})
