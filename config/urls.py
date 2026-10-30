#Rotas que o Django vai procurar (define os enderecos da pagina)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuarios.urls')),
]
