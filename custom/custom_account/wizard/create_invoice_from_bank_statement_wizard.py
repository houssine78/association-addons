from odoo import Command, models, fields
import re

class InvoiceFromBankStatementLineWizard(models.TransientModel):
    _name = 'invoice.from.statement.line'
    _description = 'Create invoice from bank statement line'

    def _default_bank_statement_line_ids(self):
        bankStatementLine = self.env['account.bank.statement.line'].sudo()
        bank_statement_line_ids = self.env.context.get('active_ids', [])
        bank_statement_lines = bankStatementLine.browse(bank_statement_line_ids)

        return [Command.link(bank_statement_line.id) for bank_statement_line in bank_statement_lines]

    invoice_date = fields.Date()
    product_id = fields.Many2one(
        "product.product",
        required=True
    )
    bank_statement_line_ids = fields.Many2many(
        comodel_name="account.bank.statement.line",
        string="Statement lines",
        default=_default_bank_statement_line_ids
    )
    account_analytic_tag_id = fields.Many2one(
        comodel_name="account.analytic.tag",
        string="Analytic tag"
    )

    def create_transition_model(self):
        resPartner = self.env['res.partner']
        statLineInvoice = self.env['statement.line.to.invoice']
         
        for statement_line in self.bank_statement_line_ids:
            stat_line_id = statLineInvoice.search([('bank_statement_line_id', '=', statement_line.id)])

            if stat_line_id:
                continue

            narration = re.sub(r"<.*?>", "", statement_line.narration)
            notes_list = narration.split('/ ')

            email = notes_list[0].strip()
            name = notes_list[1].strip()
            
            partners = resPartner.search([('email', '=', email)])
            partner_id = False
            if not partners:
                # create contact
                print()
            elif len(partners) == 1:
                partner_id = partners
            else:
                partner_id = partners.filtered(lambda r: r.is_company)
                if not partner_id:
                    partner_id = partners
                 
            vals = {
                'email': email,
                'name': name,
                'partner_id': partner_id.id if partner_id else False,
                'invoice_date': self.invoice_date,
                'product_id': self.product_id.id,
                'amount': statement_line.amount,
                'bank_statement_line_id': statement_line.id,
                'account_analytic_tag_id': self.account_analytic_tag_id.id,
                'state': 'draft',
            }

            stat_line_invoice = statLineInvoice.create(vals)
            if partner_id:
                stat_line_invoice.action_create_invoice()
