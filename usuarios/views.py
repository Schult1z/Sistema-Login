# Contem a logica do sistema
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


from .forms import CadastroForm

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Cadastro realizado com sucesso !! Agora voce ja pode logar normalmente..."
            )
            return redirect('cadastro')

    else: 
        form = CadastroForm()
        
    return render(request,'usuarios/cadastro.html', {'form': form})

def login_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        usuario = authenticate(
            request,
            username=username,
            password=senha
        )
        if usuario is not None:
            login(request, usuario)
            return redirect("home")
        else: 
            messages.error(
                request,
                "Nome de usuario ou senha invalidos"
            )
    return render(request, 'usuarios/login.html')

@login_required
def home(request):
    return render(request, "usuarios/home.html")

def logout_usuario(request):
    if request.method == "POST":
        logout(request)

    return redirect("login")
