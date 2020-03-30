================
Helpdesk Project
================

TODO:
- En la VISTA FORMULARIO DE TICKETS:

-- añadir una solapa para Project, en esa solapa:
----[Heredando la vista formulario del helpdesk_mgmt --> helpdesk_ticket_view id="ticket_view_form" --> sheet:group2:notebook:+page]

--- Poder seleccionar un proyecto o una tarea.
----[\/(tiene que añadir 2 campos m2o a project y task) ampliando la función de HelpdeskTicket por herencia con el campo project:m2o y el campo task:m2]
----[\/dentro de la página de project poniendo los dos campos seleccionables: project y task --> sin posibilidad de crear (revisar campo de seleccion de compañia)]

--- Si busco la tarea sin indicar el proyecto completar el proyecto de esa tarea
----[\/(onchange en tarea que complete el projecto)]

--- si busco primero el proyecto solo permitir seleccionar tareas de ese proyecto
----[\/(onchange a project que devuelva un domain)]

-- poder agrupar, filtrar por proyecto o tarea
----[(modificar vista search)????]

-- que aparezca en la vista kanban de los tikets, información sobre el proyechto al que pertenecen
----[Revisar vista kanban]

- En la VISTA FORMULARIO DE TAREAS[project.task]:

-- añadir una solapa para Tickets, en esa solapa:
----[\/Heredando la vista formulario del project --> notebook inside con el campo ticket_ids]
--- añadir un listado de tickets asociados a esa tarea
----[\/(o2m asociado al m2o definido en ticket)]

- MEJORAR GUI, para que:
-- [\/] las incidencias se registren en las tareas con un botón (con que datos se va a crear, pasar la tarea y proyecto por contexto)
-- [\/] se muestre un smart button con el número de incidencias y si se clicka se redirija.
-- Ver como está hecho en el módulo CRM para crear presupuestos desde leads.


DUDAS:
- Estando en helpdesk_ticket --> hay un self.project_id y un self.task_id.project_id???
- En la vista del helpdesk_mgmt la vista no esta dentro de un <data> toda la vista </data> como en el video
- Que es el domain??? para que se suele utilizar?

Proceso PR:

- Clonar el proyecto de aeodoo, dos opciones:
  - git clone git@github.com:aeodoocurso/helpdesk.git -b webinar_20200325
  - git clone https://github.com/aeodoocurso/helpdesk.git -b webinar_20200325
- Hacer un fork con vuestro usuario desde la web
- desde el directorio del proyecto puedo añadir mi remote
  git remote -v ; puedo ver mis remotes
  git remote add angelmoya https://github.com/angelmoya/helpdesk-1.git ; añado mi remote
- podría hacer directamente clone de mi proyecto, pero no viene mal tener los dos remotes
- tengo que crear una rama con otro nombre
  git checkout -b webinar_20200325_01
- despues de modificar o añadir código tengo que comitear mis cambios.
  git add .
  git commit -am "IMP ..."
- ahora subo los cambios a la rama de mi repositorio
  git push angelmoya webinar_20200325_01 ; pongo angelmoya porque es el nombre de mi remote
- El PR es como indicamos que queremos subir nuestros cambios al proyecto original,
  - los cambios los hacemos en nuestro proyecto, angelmoya
  - proponermos para subir al proyecto original, aeodoo
  - se hace desde la web:
    - con el enlace que aparece temporalmente en la web
    - o en pull/crear
