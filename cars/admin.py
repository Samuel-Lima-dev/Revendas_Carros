from django.contrib import admin
from cars.models import Car, Brand


#Adicionando as tabelas no admin do django attravés das classes

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',) 

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'value', 'year') # Campos que serão mostrado
    search_fields = ('model',) # Campo para consulta

# Registrando tabelas
admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)
