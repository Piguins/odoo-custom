from odoo import models, fields

class HelloWorld(models.Model):
    _name = 'hello.world'  # Tên model (sẽ tạo bảng hello_world trong database)
    _description = 'Hello World Model'

    name = fields.Char(string="Message", default="Hello World")