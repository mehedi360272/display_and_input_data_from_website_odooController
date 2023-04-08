from odoo import models, fields

class facultyList(models.Model):
    _name = 'se.faculty.list'
    _description = 'Faculty Information'

    name = fields.Char(string='Name :')
    phone = fields.Char(string='Phone Number:')
    email_id = fields.Char(string='Email Address:')
    is_urgent = fields.Boolean(string='Is Active?')
    date = fields.Date(string='Date:')
    subject = fields.Char(string='Subject:')
    details = fields.Char(string='Details:')
    file = fields.Binary(string="File:")
    
