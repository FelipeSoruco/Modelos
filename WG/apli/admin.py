from django.contrib import admin
from .models import Client, Persona, Proyecto, Afectacion

admin.site.register(Client)
admin.site.register(Proyecto)
admin.site.register(Persona)
admin.site.register(Afectacion)
