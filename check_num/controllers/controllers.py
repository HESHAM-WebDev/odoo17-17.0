# -*- coding: utf-8 -*-
# from odoo import http


# class IetCheckNum(http.Controller):
#     @http.route('/check_num/check_num', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/check_num/check_num/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('check_num.listing', {
#             'root': '/check_num/check_num',
#             'objects': http.request.env['check_num.check_num'].search([]),
#         })

#     @http.route('/check_num/check_num/objects/<model("check_num.check_num"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('check_num.object', {
#             'object': obj
#         })

