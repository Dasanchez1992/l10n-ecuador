# -*- coding: utf-8 -*-
from odoo import models, fields


class PosConfig(models.Model):
    _inherit = "pos.config"

    l10n_ec_auto_download_invoice = fields.Boolean(
        string="Auto descargar PDF de factura",
        default=False,
        help="Si está activado, descarga automáticamente el PDF de la factura al validar. "
        "Para Ecuador se recomienda desactivar ya que el PDF sin clave de acceso del SRI no es válido.",
    )
    l10n_ec_default_invoice = fields.Boolean(
        string="Factura por defecto",
        default=True,
        help="Si está activado, la opción de factura estará marcada por defecto en el POS.",
    )
