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

{
    'name': 'Sales Order/Quotation Print Adjust',
    'version': '1.0',
    'category': 'Sales',
    'author': 'Rooms For (Hong Kong) Limited T/A OSCG',
    'summary': 'Makes adjustments to Sales Order/Quotation print format',
    'description': """
* Makes adjustments to SO/Quotation print format
* Adds fields in SO to be printed on SO/Quotation
    """,
    'depends': ["sale"], 
    'data': [
        'views/sale_view.xml',
        'views/report_saleorder.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}

