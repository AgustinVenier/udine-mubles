from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.mail import send_mail

from django.conf import settings
from .models import User, Producto
from .forms import ProductoForm, ContactForm


def index(request):
    return render(request, "auctions/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Usuario no disponible."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def productos(request):
    productos = Producto.objects.filter(active=True)
    categorias = []
    for categoria in Producto.CATEGORIAS:
        categorias.append(categoria[1])
    return render(request, "auctions/productos.html", {
        "productos": productos,
        "categorias": categorias
    })

def producto(request, producto_id):
    producto = Producto.objects.get(pk=producto_id)
    return render(request, "auctions/producto.html", {
        "producto": producto
    })

def comprar(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            inf_form = form.cleaned_data
            send_mail(inf_form['asunto'], inf_form['mensaje'], 
            inf_form.get('email', ''), ['agusvenier04@gmail.com'],)
            return render(request, "auctions/index.html")
    else: 
        form = ContactForm()
    
    return render(request, "auctions/comprar.html", {
            "form": form
        })
        
def categoria(request, categoria):
    productos = Producto.objects.filter(active=True, categoria=categoria)
    titulo = "Productos en la categoria de " + categoria
    return render(request, "auctions/productos.html", {
        "productos": productos,
        "categoria": categoria,
        "titulo": titulo
    })