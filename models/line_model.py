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

    find_TypeProduct = fields.Selection(string="Type of the product", selection=[("m", "Merchandaising"), ("h", "Personal health"), ("s", "Supliments")], store=False)

    #Relations

    @api.constrains("quantity")
    def _checkQuantity(self):
        if self.quantity > self.product_id.stock:
            raise ValidationError("The amount of quantity is greater than the stock!!")
        else:
            self.product_id.stock -= self.quantity
            return True
    
    
    @api.onchange('find_TypeProduct')
    def onchange_genre(self):
        self.product_id = None
        if self.find_TypeProduct:
            domain = {'product_id': [('typeProduct', '=', self.find_TypeProduct)]}
        else:
            domain = {'product_id': [('typeProduct', '!=', '*ihg')]}

        return {'domain': domain}