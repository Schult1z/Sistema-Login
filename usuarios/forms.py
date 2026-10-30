#Django ja possui recursos para cadastro, incluindo validacao e senha
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import  User

# Forms fornece os campos de formulado do Django

class CadastroForm(UserCreationForm): # Formulario pronto do proprio Django para a criacao de usuarios (incluindo validacao de senha)
    email = forms.EmailField( 
        required= True,
        label= "Email"
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        labels = {
            'username' : 'Nome de usuario'
        }