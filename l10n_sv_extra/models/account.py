# -*- encoding: utf-8 -*-

from odoo import models, fields, api, _
import logging

class AccountMove(models.Model):
    _inherit = "account.move"

    tipo_gasto = fields.Selection([('compra', 'Compra/Bien'), ('servicio', 'Servicio'), ('importacion', 'Importación/Exportación'), ('combustible', 'Combustible'), ('mixto', 'Mixto')], string="Tipo de Gasto", default="compra")

class AccountJournal(models.Model):
    _inherit = "account.journal"

    direccion = fields.Many2one('res.partner', string='Dirección')
    facturas_por_rangos = fields.Boolean(string='Las facturas se ingresan por rango', help='Cada factura realmente es un rango de factura y el rango se ingresa en Referencia/Descripción')
    resolucion = fields.Char(string='Resolución')
    serie = fields.Char(string='Serie')
    rango_inicio = fields.Char(string='Rango inicio')
    rango_fin = fields.Char(string='Rango fin')
