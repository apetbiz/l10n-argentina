# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2013 E-MIPS (http://www.e-mips.com.ar) All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
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
    "name": "WSFE (Factura Electronica)",
    "version": "2.0",
    "depends": ["base", "account", "l10n_ar_point_of_sale", "l10n_ar_wsaa"],
    "author": "E-MIPS",
    "website": "http://e-mips.com.ar",
    "license": "GPL-3",
    "category": "Argentina Localization",
    "description": """
        WSFE (Web Service de Factura Electronica).
        Este módulo nos permite facturar de forma electrónica a través del Servicio Web
        que publica la AFIP.
    """,
    "init_xml": [],
    'update_xml': [
        'wsfe_data.xml',
        'wsfe_view.xml',
        'account_invoice_view.xml',
        'account_invoice_workflow.xml',
    ],
    'demo_xml': [],
    'installable': True,
    'active': False,
}
