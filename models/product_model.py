# -*- coding: utf-8 -*-
from collections import defaultdict
from odoo.exceptions import ValidationError
from odoo import models, fields, api


class productModel(models.Model):
    _name = 'gym_app.product_model'
    _description = 'Product Model'
    _sql_constraints = [('product_unique_name','UNIQUE(name)','The name of the product must be unique!!!!')]

    name = fields.Char(string="Product name", Required = True,index=True,help="Name of the Product")
    description = fields.Char(string="Product description", help="Description of the Product")
    price = fields.Float(string="Product price", Required = True,default=0,help="Price of the Product")
    photo = fields.Binary(string="Product photo", Required=True,help="The photo of the product")
    stock = fields.Integer(string="Product stock", Required = True,help="Quantity of products in the stock")

    
    #Relations
    lines_ids = fields.One2many("gym_app.line_model","product_id",string="Line")
    
    
    @api.constrains("price")
    def checkPrice(self):
        if self.price < 0:
            raise ValidationError("The price must be equal or greater than 0!!")
    
    @api.constrains("stock")
    def checkstock(self):
        if self.stock <= 0:
            raise ValidationError("The stock must be greater than 0!!")

    