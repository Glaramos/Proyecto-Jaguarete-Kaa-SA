from django.urls import path

from ProyectoApp_jaguarete_kaa import views
from django.conf import settings
from django.conf.urls.static import static
from .views import registro

urlpatterns = [
    path('',views.home, name="Home"),
    path('categorias',views.categorias, name="Categorias"),
    path('acerca_de',views.acerca_de, name="Acerca de"),
    path('contacto',views.contacto, name="Contacto"),
    path('registro/',views.registro, name="registro"),

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)