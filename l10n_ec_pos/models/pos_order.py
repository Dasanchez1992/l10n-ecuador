# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class PosOrder(models.Model):
    _inherit = 'pos.order'


    def action_pos_order_invoice(self):
        """
        Create the invoice of the pos order and validate the electronic document
        """
        res = super().action_pos_order_invoice()
        for order in self:
            if order.account_move:
                edi_format = self.env.ref(
                    "l10n_ec_account_edi.edi_format_sri", raise_if_not_found=False
                )
                if edi_format:
                    edi_format._l10n_ec_post_move_edi(order.account_move)
        return res

