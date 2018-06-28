from odoo import models, fields, api,_
from odoo.exceptions import UserError, RedirectWarning, ValidationError,except_orm
import logging

from datetime import datetime, date, time,timedelta
import datetime
import time
_logger = logging.getLogger(__name__)


class MrpWorkorder(models.Model):
    _inherit = 'mrp.workorder'
    board_id = fields.Many2one('board', string="Mesa")
    #payment = fields.Float(string="Pago de empleado por pza.")

    @api.multi
    def record_production(self):
        super(MrpWorkorder, self).record_production()
        report_ref = self.env['mrp.report.production']
        reportl_ref = self.env['mrp.report.production.line']
        for l in self.board_id.table_lines:
            x=datetime.date.today()
            #fech = '2017-01-31 00:00:00'
            #x = datetime.strptime(fech, '%Y-%m-%d %H:%M:%S').date()
            week = x.isocalendar()[1]
            print("fecha")
            print(x)
            #dicdias = {'MONDAY': '1', 'TUESDAY': '2', 'WEDNESDAY': '3', 'THURSDAY': '4', \
            #           'FRIDAY': '5', 'SATURDAY': '6', 'SUNDAY': '7'}
            #dicdias2 = {'MONDAY': '7', 'TUESDAY': '6', 'WEDNESDAY': '5', 'THURSDAY': '4', \
            #            'FRIDAY': '3', 'SATURDAY': '2', 'SUNDAY': '1'}
            #dicdias = {'MONDAY': '5', 'TUESDAY': '6', 'WEDNESDAY': '7', 'THURSDAY': '1', \
            #           'FRIDAY': '2', 'SATURDAY': '3', 'SUNDAY': '4'}
            #dicdias2 = {'MONDAY': '3', 'TUESDAY': '2', 'WEDNESDAY': '1', 'THURSDAY': '7', \
            #            'FRIDAY': '6', 'SATURDAY': '5', 'SUNDAY': '4'}
            dicdias = {'JUEVES': '1', 'VIERNES': '2', 'SABADO': '3','DOMINGO': '4', \
                       'LUNES': '5', 'MARTES': '6', 'MIERCOLES': '7'}
            dicdias2 =  {'JUEVES': '7', 'VIERNES': '6', 'SABADO': '5','DOMINGO': '4', \
                       'LUNES': '3', 'MARTES': '2', 'MIERCOLES': '1'}
            anho = x.year
            mes = x.month
            dia = x.day

            fecha = datetime.date(anho, mes, dia)
            #fecha = datetime.strptime(fech, '%Y-%m-%d %H:%M:%S')
            _logger.info(_('valos %s') % (fecha.strftime('%A')))
            noweek = dicdias[fecha.strftime('%A').upper()]
            resta = 7 - int(noweek)
            jueves = x + timedelta(days=resta)

            fecha2 = datetime.date(anho, mes, dia)
            #fecha2 = datetime.strptime(fech, '%Y-%m-%d %H:%M:%S')
            noweek2 = dicdias2[fecha2.strftime('%A').upper()]
            resta2 = 7 - int(noweek2)
            miercoles = x - timedelta(days=resta2)

            employee = l.employee_id
            report_operations = self.env['mrp.report.production'].search([('name','=',employee.id),
                                                                          ('date_start','=',miercoles),
                                                                          ('date_finish','=',jueves)], limit=1)
            if len(report_operations) == 0:
                vals = {
                    'name':employee.id,
                    'date_start':miercoles,
                    'date_finish':jueves

                }
                payment = self.operation_id.payment
                total=self.qty_produced * payment
                report_id = report_ref.create(vals)
                lines = {
                    'production_id' :report_id.id,
                    'mrp_production_id': self.production_id.id,
                    'operation_id': self.id,
                    'qty': self.qty_produced,
                    'precio_unit':payment,
                    'total':total,
                }
                reportl_ref.create(lines)
            else:
                payment = self.operation_id.payment
                total = self.qty_produced * payment
                lines = {
                    'production_id': report_operations.id,
                    'mrp_production_id': self.production_id.id,
                    'operation_id': self.id,
                    'qty': self.qty_produced,
                    'precio_unit': payment,
                    'total': total,
                }
                reportl_ref.create(lines)
