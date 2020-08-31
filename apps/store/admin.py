from django.contrib import admin
from .models import Producto, Compra, ItemsCompra

from import_export import resources
from import_export.admin import ImportExportActionModelAdmin

class ProductoResources(resources.ModelResource):
    class Meta:
        model = Producto
    
class ProductoAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    search_fields = ['nameProd', 'descripcion']
    list_display = ('nameProd', 'descripcion', 'disponible')
    resources_class = ProductoResources
    
# Register your models here.
admin.site.register(Producto, ProductoAdmin )
admin.site.register(Compra)
admin.site.register(ItemsCompra)