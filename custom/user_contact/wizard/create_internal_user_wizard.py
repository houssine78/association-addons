from odoo import api,Command, models, fields

class CreateInternalUserWizard(models.TransientModel):
    _name = 'create.internal.user.wizard'
    _description = 'Wizard to create internal users from contacts'

    def _default_partner_ids(self):
        partner_ids = self.env.context.get('active_ids', [])
        contact_ids = set()
        for partner in self.env['res.partner'].sudo().browse(partner_ids):
            contact_partners = partner.child_ids.filtered(lambda p: p.type in ('contact', 'other')) | partner
            contact_ids |= set(contact_partners.ids)

        return [Command.link(contact_id) for contact_id in contact_ids]

    contact_ids = fields.Many2many(
        'res.partner',
        string='Contacts',
        default=_default_partner_ids
    )
    create_employee = fields.Boolean()

    def create_internal_users(self):
        user_model = self.env['res.users']
        group_user = self.env.ref('base.group_user')
        for contact in self.contact_ids:
            user_values = {
                'name': contact.name,
                'login': contact.email,
                'partner_id': contact.id,
                'company_id': self.env.company.id,
                'company_ids': [(6, 0, self.env.company.ids)],
                'groups_id': [(5),(4, group_user.id)]
            }
            user = user_model.create(user_values)
            if self.create_employee:
                user.action_create_employee()

        return True
