from django.contrib import admin
from django.contrib.auth import admin as admin_add
from .models import Especialidade, Medico, Horarios, Agenda, Cliente

admin.site.register(Especialidade)
admin.site.register(Medico)
admin.site.register(Horarios)
admin.site.register(Agenda)
admin.site.register(Cliente, admin_add.UserAdmin)
