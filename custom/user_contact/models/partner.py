from odoo import models

class ResPartner(models.Model):
    _inherit = "res.partner"

    def create_user(self, partner):
        user_obj = self.env["res.users"]
        email = partner.email

        user = user_obj.search([("login", "=", email)])
        if user:
            if self.company_id not in user.company_ids:
                # add the company to the user's companies
                user.company_ids = [(4, self.company_id.id, 0)]
        else:
            # set the company as the only company of the user
            company_ids = [(6, 0, [self.company_id.id])]
            user = user_obj.search([("login", "=", email), ("active", "=", False)])
            if user:
                user.sudo().write(
                    {
                        "active": True,
                        "company_id": self.company_id.id,
                        "company_ids": company_ids,
                    }
                )
            else:
                user_values = {
                    "partner_id": partner.id,
                    "login": email,
                }
                user = user_obj.sudo()._signup_create_user(user_values)
                # passing these values in _signup_create_user() does not work
                # if the website module is loaded, because it overrides the
                # method and overwrites them.
                user.sudo().write(
                    {
                        "company_id": self.company_id.id,
                        "company_ids": company_ids,
                    }
                )
                user.sudo().with_context({"create_user": True}).action_reset_password()

        return user