from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.conf import settings
from .forms import RegisterForm

def register(request):
    template_name = 'accounts/register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate( # Fazer login do usuário após o cadastro
                username = user.username,
                password = form.cleaned_data['password1'] # Pegando o pass direto do form
            )
            login(request, user) # Login do automatico do usuário
            return redirect('core:home')
    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)