# -*- coding: utf-8 -*-
from collections import defaultdict
from odoo.exceptions import ValidationError
import re
from odoo import models, fields, api


class trainerModel(models.Model):
    _name = 'gym_app.trainer_model'
    _description = 'trainer Model'
    _sql_constraints = [('trainer_unique_dni','UNIQUE(dni)','DNI must be unique!!!!')]

    id_trainer = fields.Integer(string="trainer ID",Required=True,index=True,help="The id of the trainer")
    name = fields.Char(string="Name", Required = True,help="Name of the trainer")
    surname = fields.Char(string="Surname", Required = True,help="Surname of the trainer")
    dni = fields.Char(string="DNI", Required = True,help="DNI of the trainer", size=9)
    photo = fields.Binary(string="Picture", help="Picture of the trainer")
    phone = fields.Char(string="Phone", Required = True,help="Phone of the trainer", size=9)
    email = fields.Char(string="Email", Required = True,help="Email of the trainer")

    #Relations with client and class
    client_ids = fields.One2many("gym_app.client_model","trainer_id",string="Clients")
    class_ids = fields.One2many("gym_app.class_model","trainer_id",string="Classes")


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
