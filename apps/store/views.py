from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, ItemsCompra, Compra
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def Home(request):
    queryset = request.GET.get('buscar')
    post = Producto.objects.filter(disponible = True).order_by('nameProd')
    if queryset: 
        post = Producto.objects.filter(nameProd__icontains = queryset, disponible=True)
        
    return render(request, 'index.html', {'prdts': post})


def CompraView(request):  #Vista elementos en carrito
    prdts = None
    valCompra = None
    if request.method == 'GET': 
        try:
            orden = Compra.objects.get(cliente_id=request.user, estado=False)
            prdts = orden.itemscompra_set.all()
            valCompra = orden.get_valCompra
        except ObjectDoesNotExist:
            messages.error(request, 'Sin elementos en el carrito')
            
    return render(request, 'carrito.html', {'prdts': prdts, 'total': valCompra})
        
        
def CheckCompra(request): #Finalizacion compra
    try:
        orden = Compra.objects.get(cliente_id=request.user, estado=False)
        orden.estado = True
        orden.save()
        messages.error(request, 'Compra finalizada con exito')
            
    except ObjectDoesNotExist:
        messages.error(request, 'No se pudo finalizar La compra')

    return redirect('store:pg_Carrito_View')
        
        
def AddCard(request, id): #Añadir articulos al carrito
    
    prdt = get_object_or_404(Producto, pk=id)
    compra_qr = Compra.objects.filter(cliente_id = request.user, estado = False) #ALGUNA COMPRA PENDIENTE
    
    if prdt.cantidad > 0:
        
        if compra_qr.exists(): 
            compra = compra_qr[0] #saco la instancia con la que estoy trabajando
            
            if compra.itemscompra_set.filter(producto_id=prdt).exists():
                item = compra.itemscompra_set.get(producto_id = prdt)
                item.cantidad += 1 #AUMENTO DE 1 EN UNO LA CANTIDAD DE PRODCTOS
                item.precio = item.cantidad * prdt.precio_vnt
                item.save()
                
                prdt.cantidad -=1 #dISMINUYO EL STOCK DEL PRODUCTO
                prdt.save()
                messages.success(request, 'Añadido a carrito')
            else: 
                compra.itemscompra_set.create(producto_id=prdt, cantidad=1, precio=prdt.precio_vnt)  # Añado el nuevo elemento
                
                prdt.cantidad -= 1  # DISMINUYO EL STOCK DEL PRODUCTO
                prdt.save()
                messages.success(request, 'Añadido a carrito')
        else:     
            compra = Compra.objects.create(cliente_id = request.user) #Creo una compra nueva
            compra.itemscompra_set.create(producto_id = prdt, cantidad = 1, precio = prdt.precio_vnt) #Añado el nuevo elemento
            
            prdt.cantidad -= 1  #DISMINUYO EL STOCK DEL PRODUCTO
            prdt.save()
            messages.success(request, 'Añadido a carrito')
    else:       
        messages.error(request, 'No hay mas stock')        
        
    return redirect('store:pg_Carrito_View')       


def EliminarCarrito(request, id):  #Eliminar Elmento del carrito
    
    prdt = get_object_or_404(Producto, pk=id)
    compra_qr = Compra.objects.filter(cliente_id = request.user, estado = False) #ALGUNA COMPRA PENDIENTE
    if compra_qr.exists():
        compra = compra_qr[0]  # saco la instancia con la que estoy trabajando

        if compra.itemscompra_set.filter(producto_id=prdt).exists():
            item = compra.itemscompra_set.get(producto_id=prdt)
            item.cantidad -= 1  # disminuye DE 1 EN 1 LA CANTIDAD DE PRODCTOS
            if item.cantidad > 0: 
                item.precio = item.cantidad * prdt.precio_vnt
                item.save()
            else: 
                item.delete()
                
            prdt.cantidad += 1  # aumento EL STOCK DEL PRODUCTO
            prdt.save()
            messages.success(request, 'Eliminado del carrito')
            
    return redirect('store:pg_Carrito_View')  
    
