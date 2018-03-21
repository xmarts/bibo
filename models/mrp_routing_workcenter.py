from odoo import models, fields, api

class MrpRoutingWorkorder(models.Model):
    _inherit = 'mrp.routing.workcenter'
    payment = fields.Float(string="Pago de empleado por pza.")