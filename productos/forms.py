from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["nombre","categorias","descripcion","imagen","precio"]
        # fields= '__all__'
