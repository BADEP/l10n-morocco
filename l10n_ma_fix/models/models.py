# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class l10n_ma_fix(models.Model):
#     _name = 'l10n_ma_fix.l10n_ma_fix'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

def _migrate_existing_data():
    pass

class AccountAccount(models.Model):
    _inherit = 'account.account'

    @api.model
    def init_migration(self):
        for company in self.env['res.company'].search([]):
            self.env['ir.property'].search([('name', '=', 'property_account_receivable_id'), ('company_id', '=', company.id)]).write({
                'value_reference': 'account.account,' + str(self.env.ref('l10n_ma.' + str(company.id) +'_pcg_34211').id)})
            self.env['ir.property'].search([('name', '=', 'property_account_payable_id'), ('company_id', '=', company.id)]).write({
                'value_reference': 'account.account,' + str(self.env.ref('l10n_ma.' + str(company.id) +'_pcg_4411').id)})
            self.env['ir.property'].search([('name', '=', 'property_account_expense_categ_id'), ('company_id', '=', company.id)]).write({
                'value_reference': 'account.account,' + str(self.env.ref('l10n_ma.' + str(company.id) +'_pcg_6111').id)})
            company.write({
                'account_sale_tax_id': self.env.ref('l10n_ma.' + str(company.id) +'_tva_vt20').id,
                'account_purchase_tax_id': self.env.ref('l10n_ma.' + str(company.id) +'_tva_ac20').id,
            })