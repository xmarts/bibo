from odoo import models, fields, api

class BiboProductTemplate(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    ref_bibo = fields.Char('Referencia')

class AccountInvoice(models.Model):
    _name = 'account.invoice'
    _inherit = 'account.invoice'

    @api.one
    def _compute_count_line(self):
        self.count_line = len(self.invoice_line_ids)

    count_line = fields.Integer(String='Cantidad de lineas de la factura', compute='_compute_count_line')

class DebtCustomerReport(models.AbstractModel):
    _name = 'report.debt_customer.customer_debt_report'


    @api.model
    def render_html(self, docids, data=None):
        """Render report template"""
        report_obj = self.env['report']
        report = report_obj._get_report_from_name('debt_customer.customer_debt_report')

        docargs = {
            'doc_ids': docids,
            'doc_model': report.model,
            'docs': data['form'],
            'dates': data['dates'],
        }

        return report_obj.render('debt_customer.customer_debt_report', docargs)
