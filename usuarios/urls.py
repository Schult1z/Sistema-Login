
from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_usuario, name="inicio"),
    path("login/", views.login_usuario, name="login"),
    path("cadastro/", views.cadastro, name="cadastro"),
    path("home/", views.home, name="home"),
    path("logout/", views.logout_usuario, name="logout"),
]
