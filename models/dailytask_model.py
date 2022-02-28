# -*- coding: utf-8 -*-
from collections import defaultdict
from odoo.exceptions import ValidationError
from odoo import models, fields, api


class dailytaskmodel(models.Model):
    _name = 'gym_app.dailytask_model'
    _description = 'Daily Model'

    name = fields.Char(string="Task name", Required = True,index=True,help="Name of the task")
    description = fields.Char(string="Task description", help="Description of the task")
    times = fields.Integer(string="Times per week",Required=True,help="Put the time of the tas k per week")

    
    #Relations
    routine_ids = fields.Many2many("gym_app.routine_model",string="Routines")
    
   