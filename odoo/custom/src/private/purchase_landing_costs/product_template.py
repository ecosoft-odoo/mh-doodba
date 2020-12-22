#  -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2012 OpenERP s.a. (<http://www.openerp.com>).
#    Copyright (C) 2012 Mentis d.o.o. (<http://www.mentis.si>)
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

from openerp.osv import fields, osv
        

#----------------------------------------------------------
# Product INHERIT
#----------------------------------------------------------
class product_template(osv.osv):
    _inherit = "product.template"
    _columns = {
        'landing_cost'               : fields.boolean('Landing Cost',  help="Used if this product is landing cost"),
        'landing_cost_calculate'     : fields.boolean('Calculate Landing Costs', help="Check this if you want to use landing cost calculation for average price for this product"), 
    }
    _defaults = {
        'landing_cost': lambda *a: False,
        'landing_cost_calculate': lambda *a: True,
    }

product_template()
