from odoo import models, api, fields, _

class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"


    project_id = fields.Many2one(
        string="Project name",
        comodel_name="project.project")

    task_id = fields.Many2one(
        string="Task name",
        comodel_name="project.task")

    # Si busco la tarea sin indicar el proyecto completar el proyecto de esa tarea
    @api.onchange("task_id")
    def _onchange_task_id(self):
        if self.task_id and self.task_id.project_id:
            self.project_id = self.task_id.project_id
        else:
            self.project_id = False

    # Si busco primero el proyecto solo permitir seleccionar tareas de ese proyecto
    @api.onchange("project_id")
    def _onchange_project_id(self):
        if self.project_id:
            domain = {'task_id':[('project_id', '=', self.project_id.id)]}
        else:
            domain = {}

        return {"domain":domain}
