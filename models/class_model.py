# -*- coding: utf-8 -*-
from collections import defaultdict
from odoo.exceptions import ValidationError
from odoo import models, fields, api


class classModel(models.Model):
    _name = 'gym_app.class_model'
    _description = 'class Model'

    #Se hace con un wizard que al darle yo name y date me cree automaticaente las clases

    name = fields.Char(string="class name", Required = True,index=True,help="Name of the class")
    description = fields.Char(string="class description", help="Description of the class")
    photo = fields.Binary(string="Picture", help="Picture of the routine")

    #Debo controlar que no se añada la clase 
    #date = fields.Date(string="Date of the class",Required = True,help="The date of the class")

    
    #Relations with trainer and client(many2many)
    client_ids = fields.Many2many("gym_app.client_model",string="Clients")
    trainer_id = fields.Many2one("gym_app.trainer_model", string="Trainer")
    
    