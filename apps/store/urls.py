from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import CompraView, CheckCompra, AddCard, EliminarCarrito

urlpatterns = [
    path('carrito-View/', login_required(CompraView), name = 'pg_Carrito_View'),
    path('carrito/confir-compra/', login_required(CheckCompra), name = 'pg_Carrito_Check'),
    path('add-item/<int:id>/', login_required(AddCard), name = 'pg_Carrito_Add'),
    path('delt-item/<int:id>/', login_required(EliminarCarrito), name='pg_Carrito_Del'),
]
