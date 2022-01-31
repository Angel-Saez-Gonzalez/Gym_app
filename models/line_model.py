# -*- coding: utf-8 -*-
from collections import defaultdict
from itertools import product
from odoo.exceptions import ValidationError
from odoo import models, fields, api


class lineModel(models.Model):
    _name = 'gym_app.line_model'
    _description = 'Line Model'

    quantity = fields.Integer(string="Quantity", Required = True,help="Quantity of products in the line")
    invoice_id = fields.Many2one("gym_app.invoice_model", string="Invoice")
    product_id = fields.Many2one("gym_app.product_model", string="Product")

    #Relations

    @api.constrains("quantity")
    def _checkQuantity(self):
        if self.quantity > self.product_id.stock:
            raise ValidationError("The amount of quantity is greater than the stock!!")
        else:
            self.product_id.stock -= self.quantity
            return True
    
    
