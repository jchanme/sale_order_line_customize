# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PurchaseLineNumber(models.Model):

        _inherit='purchase.order.line'

        x_line_no = fields.Integer()
        x_tag_no = fields.Char()
