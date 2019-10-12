from django.contrib import admin
from apps.menu.models import Producto, Categoria
from apps.pedidos.models import Pedidos, Mesa

# Register your models here.
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Pedidos)
admin.site.register(Mesa)
