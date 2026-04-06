/** @odoo-module */

import { Order } from "@point_of_sale/app/store/models";
import { patch } from "@web/core/utils/patch";

patch(Order.prototype, {
    setup(_defaultObj, options) {
        super.setup(...arguments);
        // Set invoice as default if configured for Ecuador
        if (this.pos.config.l10n_ec_default_invoice) {
            this.to_invoice = true;
        }
    },
});
