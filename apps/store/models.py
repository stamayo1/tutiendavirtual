from django.db import models
from django.contrib.auth.models import User

# Create your models 
class Producto(models.Model):
    
    nameProd = models.CharField('Nombre producto', max_length = 80, blank = False, null = False )
    descripcion = models.CharField('Breve descripcion', max_length = 70, blank = False, null = False, default= "")
    costoProducto =  models.FloatField('Precio de compra', default= 0.0)
    precio_vnt = models.FloatField('Precio venta', default = 0.0)
    imagen = models.URLField('URL imagen', max_length=286, blank = False, null = False)
    disponible = models.BooleanField('Producto Activo/Inactivo', default = True)
    fecha_creacion = models.DateField('Fecha registro', auto_now = False, auto_now_add = True)
    cantidad = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return self.nameProd

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        
        
class Compra(models.Model):
    cliente_id = models.ForeignKey(User, on_delete = models.SET_NULL, blank = False, null = True)
    fecha_compra = models.DateField('Fecha compra', auto_now_add = True)
    estado = models.BooleanField('proceso Completado', default = False)
    dirc = models.CharField('Direccion entrega', max_length = 50, blank = False, null = False, default='Calle/Av')
    
    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
    
    @property
    def get_valCompra(self): 
        items= self.itemscompra_set.all()
        total = sum([item.precio for item in items ]) 
        return total

class ItemsCompra(models.Model):
    compra_id = models.ForeignKey(Compra, on_delete = models.SET_NULL, blank = False, null = True)
    producto_id = models.ForeignKey(Producto, on_delete = models.SET_NULL, blank = False, null = True)
    cantidad = models.PositiveIntegerField('Cantidad comprada', default = 0)
    precio = models.FloatField('Precio venta', default=0.0)
    fecha_compra = models.DateField('Fecha compra producto', auto_now_add = True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'ItemCompra'
        verbose_name_plural = 'Items Compra'
    
        
