from django.urls import path

from  .import views

urlpatterns = [
    path('',views.productos, name="Productos"),
    path('agregar_producto/',views.agregar_producto, name="agregar_producto"),
    path('listar_productos/',views.listar_productos, name="listar_productos"),
    path('buscar_producto/',views.buscar_producto, name="buscar_producto"),
    path('modificar_producto/<id>/',views.modificar_producto,name="modificar_producto"),    
    path('eliminar_producto/<id>/',views.eliminar_producto,name="eliminar_producto"), 
]

