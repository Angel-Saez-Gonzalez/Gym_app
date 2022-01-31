# -*- coding: utf-8 -*-
from collections import defaultdict
from datetime import datetime
from xmlrpc import client
from odoo.exceptions import ValidationError
import re
from odoo import models, fields, api


class invoiceModel(models.Model):
    _name = 'gym_app.invoice_model'
    _description = 'Invoice Model'
    _sql_constraints = [('invoice_unique_ref','UNIQUE(reference)','The Ref must be unique!!!!')]

    reference = fields.Integer(string="Ref", Required = True,index=True,help="Reference of the Invoice")
    date = fields.Date(string="Date",default=datetime.now(),help="Date ofcreation of the Invoice")
    base = fields.Float(string="Base", Required = True,help="Total price without VAT",compute="_checkBase",store="true")
    vat = fields.Selection(string="VAT",selection=[('0','0'),('4','4'),('10','10'),('21','21')],default='21', help="VAT")
    total = fields.Float(string="Total", Required = True,help="Total price with VAT",compute="_checkTotal",store="true")



    #Atributo state para cambiar el estado de la factura
    state = fields.Selection(string="Status",selection=[('draft', 'Draft'),('confirmed', 'Confirmed')], default="draft")

    #Relations

    lines_ids = fields.One2many("gym_app.line_model","invoice_id",string="Line")
    client_id = fields.Many2one("gym_app.client_model",string="Client")

    #Functions
    @api.depends("lines_ids")
    def _checkBase(self):
        sum = 0
        for line in self.lines_ids:
            sum += line.product_id.price * line.quantity
        self.base = sum
        return True

    @api.depends("base","vat")
    def _checkTotal(self):
        self.total = self.base*int(self.vat)/100.0 + self.base
        return True



    #Boton qye cambia el estado
    def confirm_request(self):
        self.ensure_one()
        #Se hace una transaccion para que si salta un error no se guarden los cambios realizados
        self._cr.autocommit(False)
        self.state= "confirmed"
        for rec in self.lines_ids:
            if rec.quantity <= rec.product_id.stock:
               rec.product_id.stock -= rec.quantity
            else:
                self._cr.rollback()
                raise ValidationError("There is no Stock of "+rec.product_id.name+"!")
        #Se hace el commit          
        self._cr.commit()
        #El autocommit lo volvemos true
        self._cr.autocommit(True)
        return True

    #def _get_id(self):
        #return (self.env['invoice_app.invoice_model'].search([])[-1].id + 1)