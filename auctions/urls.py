from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("productos", views.productos, name="productos"),
    path("comprar", views.comprar, name="comprar"),
    path("producto/<int:producto_id>", views.producto, name="producto"),
    path("productos/<str:categoria>", views.categoria, name="categoria")
]
