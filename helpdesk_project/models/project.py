from odoo import models, api, fields, _

class ProjectTask(models.Model):
    _inherit = "project.task"

    # One2many field; the value of such a field is the recordset of all the
    # records in comodel_name such that the field inverse_name is equal to the
    # current record.
    ticket_ids = fields.One2many(
        string="Tickets",
        comodel_name="helpdesk.ticket",
        inverse_name="task_id")
