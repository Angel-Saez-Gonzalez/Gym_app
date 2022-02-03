# -*- coding: utf-8 -*-
from collections import defaultdict
from odoo.exceptions import ValidationError
from odoo import models, fields, api


class dailytaskmodel(models.Model):
    _name = 'gym_app.dailytask_model'
    _description = 'Daily Model'

    name = fields.Char(string="Task name", Required = True,index=True,help="Name of the task")
    description = fields.Char(string="Task description", help="Description of the task")
    date = fields.Date(string="Date of the tasks",Required=True,help="Put the date of the task you wanna complete")

    
    #Relations
    client_ids = fields.Many2many("gym_app.client_model",string="Clients")
    
   