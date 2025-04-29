# -*- coding: utf-8 -*-
# from odoo import http


# class Levelup(http.Controller):
#     @http.route('/levelup/levelup', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/levelup/levelup/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('levelup.listing', {
#             'root': '/levelup/levelup',
#             'objects': http.request.env['levelup.levelup'].search([]),
#         })

#     @http.route('/levelup/levelup/objects/<model("levelup.levelup"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('levelup.object', {
#             'object': obj
#         })

