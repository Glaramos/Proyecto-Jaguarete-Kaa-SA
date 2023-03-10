from django.shortcuts import render,redirect, HttpResponse
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.

def home(request):

    return render(request,"ProyectoApp_jaguarete_kaa/home.html")

def categorias(request):

    return render(request,"ProyectoApp_jaguarete_kaa/categorias.html")

def acerca_de (request):

    return render(request,"ProyectoApp_jaguarete_kaa/acerca_de.html")

def contacto(request):

    return render(request,"ProyectoApp_jaguarete_kaa/contacto.html")

def registro(request):
    data={
        'form':CustomUserCreationForm()
    }

    if request.method =='POST':
        formulario = CustomUserCreationForm (data=request.POST)
        if formulario.is_valid():
             formulario.save()
             user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
             login(request,user)
             messages.success(request,"Te has registrado correctamente")
             return redirect(to="Home")

        data["form"]= formulario

    return render(request,"registration/registro.html",data)






