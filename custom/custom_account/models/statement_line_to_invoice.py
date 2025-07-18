from odoo import fields, models, _
from odoo.exceptions import UserError


class StatementLineToInvoice(models.Model):
    _name = 'statement.line.to.invoice'
    _description = 'Transition model to track invoice creation from statement'

    email = fields.Char(
        required=True
    )
    name = fields.Char()
    partner_id = fields.Many2one(
        "res.partner",
    )
    invoice_date = fields.Date()
    product_id = fields.Many2one(
        "product.product",
        required=True
    )
    journal_id = fields.Many2one(
        'account.journal',
        required=True
    )
    currency_id = fields.Many2one(
        comodel_name='res.currency',
        related='bank_statement_line_id.currency_id',
    )
    amount = fields.Monetary()
    bank_statement_line_id = fields.Many2one(
        "account.bank.statement.line",
        string="Statement line",
        required=True
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
        required=True
    )
    error_msg = fields.Char(string="Error message")

    def action_create_invoice(self):
        self.ensure_one()

        if not self.partner_id:
            raise UserError(_('this line has no partner'))

        accountMove = self.env['account.move']
        moveLine = self.env['account.move.line']

        move_vals = {
            "move_type": "out_invoice",
            "invoice_date": self.invoice_date,
            "partner_id": self.partner_id.id,
            "journal_id": self.journal_id.id
        }

        move = accountMove.create(move_vals)
        line_vals = {
            "move_id": move.id,
            "product_id": self.product_id.id,
            "analytic_tag_ids": [self.account_analytic_tag_id.id],
        }

        if self.amount > self.product_id.lst_price:
            line_vals['price_unit'] = self.amount

        self.write({"state": "invoiced", "invoice_id": move.id})

    def action_assign_partner(self):
        self.ensure_one()

        resPartner = self.env['res.partner']
        partners = resPartner.search([('email', '=', self.email)])

        partner_id = False
        if not partners:
            partner_vals = {
                'email': self.email,
                'name': self.name,
                'is_company': False
            }
            partner_id = resPartner.create(partner_vals)

        elif len(partners) == 1:
            partner_id = partners
        else:
            partner_id = partners.filtered(lambda r: r.is_company)
            if not partner_id:
                partner_id = partners

        self.partner_id = partner_id
