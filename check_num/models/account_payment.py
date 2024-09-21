from odoo import fields, models, api


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    check_number = fields.Char(string='Check Number', readonly=False)





