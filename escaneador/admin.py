from django.contrib import admin
from .models import Escaneador, Operacion

# Register your models here.

class EscaneadorAdmin(admin.ModelAdmin):
    pass

class OperacionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Escaneador, EscaneadorAdmin)
admin.site.register(Operacion, OperacionAdmin)