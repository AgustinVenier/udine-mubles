from django.forms import ModelForm, Form
from .models import User, Producto
from django import forms

class ProductoForm(ModelForm):
    class Meta():
        model = Producto
        fields = ['titulo', 'descripcion', 'precio', 'imagen_url', 'categoria']
        labels = {
            'descripcion': 'Descripción',
            'precio': 'Precio',
            'categoria': 'Categorias'
        }

class ContactForm(forms.Form):
    asunto = forms.CharField()
    email = forms.EmailField()
    mensaje = forms.CharField()