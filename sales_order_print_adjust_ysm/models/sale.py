# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) Rooms For (Hong Kong) Limited T/A OSCG (<http://www.openerp-asia.net>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import _
from openerp.osv import fields, osv

class sale_order(osv.osv):
    _inherit = "sale.order"
    
    _columns = {
        'expiry_date': fields.date(_('Expiration Date'), select=True, help=_("Until the date this quotation is available.")),
        'trade_policy': fields.selection([
            ('package', _('Package Purchase')),
            ('month', _('Cutoff at Month-End')),
            ('next', _('Cutoff at Next-Month-End')),
            ('part', _('Part Purchase')),
            ], _('Transaction Method')),
        'deliver_limit': fields.char(_('Delivery Deadline'), help=_("In the period products will be delivered.")),
    }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

