# -*- coding: utf-8 -*-
from odoo import http

# class CursoOdoo/odooPractica(http.Controller):
#     @http.route('/curso_odoo/odoo_practica/curso_odoo/odoo_practica/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/curso_odoo/odoo_practica/curso_odoo/odoo_practica/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('curso_odoo/odoo_practica.listing', {
#             'root': '/curso_odoo/odoo_practica/curso_odoo/odoo_practica',
#             'objects': http.request.env['curso_odoo/odoo_practica.curso_odoo/odoo_practica'].search([]),
#         })

#     @http.route('/curso_odoo/odoo_practica/curso_odoo/odoo_practica/objects/<model("curso_odoo/odoo_practica.curso_odoo/odoo_practica"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('curso_odoo/odoo_practica.object', {
#             'object': obj
#         })