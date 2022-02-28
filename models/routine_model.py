# -*- coding: utf-8 -*-
from collections import defaultdict
from odoo.exceptions import ValidationError
from odoo import models, fields, api


class routineModel(models.Model):
    _name = 'gym_app.routine_model'
    _description = 'routine Model'
    _sql_constraints = [('routine_unique_name','UNIQUE(name)','The name of the routine must be unique!!!!')]

    id_routine = fields.Integer(string="Routine ID",Required=True,index=True,help="The id of the routine",default=lambda self: self._get_id())
    name = fields.Char(string="routine name", Required = True,index=True,help="Name of the routine")
    description = fields.Char(string="routine description", help="Description of the routine")
    photo = fields.Binary(string="Picture", help="Picture of the routine")

    
    #Relations
    client_ids = fields.One2many("gym_app.client_model","routine_id",string="Clients")
    dailytask_ids = fields.Many2many("gym_app.dailytask_model",string="Tasks")
    
    
    def _get_id(self):
          if len(self.env['gym_app.routine_model'].search([])) == 0:
               return 1
          return (self.env['gym_app.routine_model'].search([])[-1].id + 1)