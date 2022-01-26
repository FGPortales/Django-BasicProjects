from django.contrib import admin
from gestionPedidos.models import Clientes, Articulos, Pedidos

# Register your models here.


class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono')  # Para agregar campos en la vista(lista del modelo)
    search_fields = ('nombre', 'telefono')  # Para hacer busquedas(por nombre y telefono) en el modelo


class ArticulosAdmin(admin.ModelAdmin):
    list_filter = ('seccion',)


class PedidosAdmin(admin.ModelAdmin):
    list_display = ('numero', 'fecha')
    list_filter = ('fecha',)
    date_hierarchy = 'fecha'


admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin)
