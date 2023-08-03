from django.contrib import admin
from .models import analisis, especialidad, examen, medico, usuario, rol, paciente
# Register your models here.


admin.site.register(analisis)
admin.site.register(especialidad)
admin.site.register(examen)
admin.site.register(medico)
admin.site.register(usuario)
admin.site.register(rol)
admin.site.register(paciente)

