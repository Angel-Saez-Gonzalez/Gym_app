# -*- coding: utf-8 -*-
# from odoo import http


# class GymApp(http.Controller):
#     @http.route('/gym_app/gym_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gym_app/gym_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gym_app.listing', {
#             'root': '/gym_app/gym_app',
#             'objects': http.request.env['gym_app.gym_app'].search([]),
#         })

#     @http.route('/gym_app/gym_app/objects/<model("gym_app.gym_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gym_app.object', {
#             'object': obj
#         })
