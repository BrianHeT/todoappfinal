from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "descripcion", "completado",)
    
    
    
admin.site.register(Todo,TodoAdmin)
    
    
