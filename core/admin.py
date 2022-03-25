from django.contrib import admin

from .models import Cargo, Chef

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
   list_display = ('cargo', 'ativo', 'modificado')
 
@admin.register(Chef)  
class ChefAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'modificado')