from django.contrib import admin
from .models import Planta, Cultivo, Germinacion

# Register your models here.
admin.site.register(Planta)
admin.site.register(Cultivo)
admin.site.register(Germinacion)