# Copyright 2021 Sergio Teruel <sergio.teruel@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class AccountMove(models.Model):
    _inherit = "account.move"

    def _get_margin_applicable_lines(self):
        lines = super()._get_margin_applicable_lines()
        return lines.filtered(lambda x: not x.sale_line_ids.is_downpayment)
