from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from django.db.models import Q
# from .forms import contactoForm, ProductoForm
from django.contrib import messages 
from .forms import ProductoForm 

#from carro.carro import Carro

# Create your views here.

def productos(request):    
    
    #carro=Carro(request)
    productos=Producto.objects.all()

    return render(request, "productos/Productos.html", {"productos":productos})

def agregar_producto(request):  

    data= {
         
         'form': ProductoForm()
     
    }

    if request.method=='POST':
       formulario = ProductoForm(data=request.POST, files=request.FILES)
       if formulario.is_valid():
          formulario.save()
          messages.success(request,"Producto Registrado")
       else:
            data["form"]=formulario

    return render(request, "productos/agregar_Producto.html",data)

def listar_productos(request): 

    productos=Producto.objects.all()       

    return render(request, "productos/listar_Productos.html", {"productos":productos})   

def modificar_producto(request, id):

    producto = get_object_or_404(Producto, id =id)

    data ={
        'form' : ProductoForm(instance=producto)
    }

    if request.method=='POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files = request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Modificado Correctamente")
            return redirect(to ="listar_productos") 
        data["form"]=formulario

    return render(request, 'productos/modificar_Producto.html',data)

def eliminar_producto(request,id):
    producto = get_object_or_404(Producto, id =id)
    producto.delete()
    messages.success(request,"Eliminado Correctamente")
    return redirect(to="listar_productos") 

def buscar_producto(request): 

    busqueda = request.POST.get("buscar")
    productos=Producto.objects.all()   

    if busqueda:
         productos=Producto.objects.filter(
             Q(nombre__icontains=busqueda)
         ).distinct()    

   
    return render(request, "productos/listar_Productos.html", {"productos":productos})   


