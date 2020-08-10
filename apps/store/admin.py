from django.contrib import admin
from .models import Producto, Compra, ItemsCompra

# Register your models here.
admin.site.register(Producto)
admin.site.register(Compra)
admin.site.register(ItemsCompra)