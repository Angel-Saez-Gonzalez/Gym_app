# -*- coding: utf-8 -*-
from collections import defaultdict
from odoo.exceptions import ValidationError
import re
from odoo import models, fields, api


class clientModel(models.Model):
    _name = 'gym_app.client_model'
    _description = 'Client Model'
    _sql_constraints = [('client_unique_dni','UNIQUE(dni)','DNI must be unique!!!!')]

    id_client = fields.Integer(string="Client ID",Required=True,index=True,help="The id of the client")
    name = fields.Char(string="Name", Required = True,help="Name of the Client")
    surname = fields.Char(string="Surname", Required = True,help="Surname of the Client")
    dni = fields.Char(string="DNI", Required = True,help="DNI of the Client", size=9)
    photo = fields.Binary(string="Picture", help="Picture of the Client")
    phone = fields.Char(string="Phone", Required = True,help="Phone of the Client", size=9)
    email = fields.Char(string="Email", Required = True,help="Email of the Client")
    subscription = fields.Selection(string="Type of subscription",selection=[('basic','Basic Subscription'),('advance','Advanced Subscription'),('premium','Premium Subscription')],default='basic', help="Type of subscription of the GYM")

    #Relations with invoice class tasks y trainer
    invoice_ids = fields.One2many("gym_app.invoice_model","client_id",string="Invoices")
    trainer_id = fields.Many2one("gym_app.trainer_model",string="Trainer")
    dailytask_ids = fields.Many2many("gym_app.dailytask_model",string="Task")

    #Este deberia ser Many2Many
    class_ids = fields.Many2many("gym_app.class_model",string="Class")

    @api.constrains("dni")
    def comprNIF(self):
        tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
        numeros = "1234567890"
        nif = self.dni
        respuesta = "No ha introducido un NIF valido"
        if (len(nif) == 9):
            letraControl = nif[8].upper()
            dn = nif[:8]
            if ( len(dn) == len( [n for n in dn if n in numeros] ) ):
                if tabla[int(dn)%23] == letraControl:
                    return True
        raise ValidationError("The DNI is not valid")

    
    @api.constrains("email")
    def comprEmail(self):
    
        correo = self.email

        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
    
        if(re.search(regex,correo)):   
            print("Valid Email")  
            return True

        else:   
            raise ValidationError("The patient email is not valid")
