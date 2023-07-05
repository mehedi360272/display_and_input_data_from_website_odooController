# -*- coding: utf-8 -*-
# class Faculty(http.Controller):
#     @http.route('/he', type='http', auth='public', website=True)
#     def se_faculty(self, **kw):
#         return "hello"

from odoo import http
from odoo.http import request


class MyController(http.Controller):

    @http.route('/help', type='http', auth='public', website=True)
    def my_controller(self, **kw):
        my_data = request.env['se.faculty.list'].search([])
        return request.render('display_and_input_data_from_website_odooController.help_page', {
            'my_data': my_data,
        })

class MyController2(http.Controller):
    # Render Form View
    @http.route('/help/form', auth='public', website=True)
    def new_form(self, **kw):
        return request.render('display_and_input_data_from_website_odooController.add_info', {
        })

    # Redirect To  the Page
    @http.route('/help_form', auth='public', website=True)
    def info_redirect(self, **kw):
        name = kw.get('name')
        phone = kw.get('phone')
        email = kw.get('email_id')
        is_urgent = kw.get('is_urgent')
        date = kw.get('date')
        subject = kw.get('subject')
        details = kw.get('details')
        file = kw.get('file')

        request.env['se.faculty.list'].create({
            'name': name,
            'phone': phone,
            'email_id': email,
            'is_urgent': is_urgent,
            'date': date,
            'subject': subject,
            'details': details,
            'file': file,
        })
        redirect = '/help'
        return request.redirect(redirect)
