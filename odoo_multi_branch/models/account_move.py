# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    company_branch_id = fields.Many2one(
        'res.company.branch',
        string="Branch",
        copy=False,
    )

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: