# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleLineNumber(models.Model):

        _inherit='sale.order.line'

        x_line_no = fields.Integer(string='No.')
        x_tag_no = fields.Char(string='Tag No.')
        x_price_unit = fields.Monetary(compute='_compute_price', string='New Price', readonly=True, store=True)
        x_notes = fields.Text(string='Notes', translate=True)

        @api.depends('discount', 'price_unit')
        def _compute_price(self):
                """
                Compute the amounts of the SO line.
                """
                for line in self:
                        line.x_price_unit = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
