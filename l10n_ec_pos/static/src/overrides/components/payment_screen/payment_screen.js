/** @odoo-module */

import { patch } from "@web/core/utils/patch";
import { PaymentScreen } from "@point_of_sale/app/screens/payment_screen/payment_screen";

patch(PaymentScreen.prototype, {
    /**
     * Override to control automatic PDF download based on Ecuador configuration.
     * For Ecuador, the invoice PDF without SRI access key is not valid,
     * so we disable automatic download by default.
     */
    shouldDownloadInvoice() {
        if (this.pos.config.l10n_ec_auto_download_invoice === false) {
            return false;
        }
        return super.shouldDownloadInvoice();
    },
});
