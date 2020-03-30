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

    ticket_count = fields.Integer(compute='_compute_ticket_data',
                                  string="Number of Tickets")

    @api.depends('ticket_ids')
    def _compute_ticket_data(self):
        for task in self:
            print(task)
            task.ticket_count = len(task.ticket_ids)



    def action_new_ticket(self):
        action = self.env.ref("helpdesk_project.task_action_ticket_new").read()[0]
        action['context'] = {
        # diccionario con los datos
        'default_task_id': self.id,
        'default_project': self.project_id and self.project_id.id
        }
        return action


    def action_view_tickets(self):
        action = self.env.ref('helpdesk_project.action_view_tickets').read()[0]
        action['context'] = {
            'default_opportunity_id': self.id
        }
        action['domain'] = [('opportunity_id', '=', self.id), ('state', 'in', ['draft', 'sent'])]
        if len(quotations) == 1:
            action['views'] = [(self.env.ref('sale.view_order_form').id, 'form')]
            action['res_id'] = quotations.id
        return action
