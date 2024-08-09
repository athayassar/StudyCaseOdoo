# -*- coding: utf-8 -*-
from odoo import models, fields, api

class TrainTransportation(models.Model):
    _name = 'train.transportation'
    _description = 'Train Transportation'

    name = fields.Char(string='Train', required=True)
    description = fields.Text(string='Kota')
    user_id = fields.Many2one('res.users', string="Masinis")
    session_line = fields.One2many('train.schedule', 'course_id', string='Schedule')

class TrainSchedule(models.Model):
    _name = 'train.schedule'
    _description = 'Train Schedule'

    course_id = fields.Many2one('train.transportation', string='Schedule', required=True, ondelete='cascade')
    name = fields.Char(string='Nama', required=True)
    start_date = fields.Date(string='Tanggal Keberangkatan')
    seats = fields.Integer(string='Kursi', help='Jumlah Kuota Kursi')
    partner_id = fields.Many2one('res.partner', string='Masinis')