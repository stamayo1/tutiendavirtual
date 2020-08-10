from django.shortcuts import render, redirect
from .forms import ClienteForm
from django.contrib.auth import  login as auth_login, logout
from django.contrib.auth.models import User

from django.contrib import messages

# Create your views here.
def Login(request): 
    
    if request.method == 'POST': 
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email= email)
            if user.check_password(password):
              auth_login(request, user)
              return redirect('pg_Home')
            else: 
                messages.error(request, 'las contraseñas no coinciden')
              
        except User.DoesNotExist:
            messages.error(request, 'Usuario no encontrado')
        
    return render(request, 'login.html')

def Logout(request):
    logout(request)
    return redirect('pg_Home')

def SingIn(request):

    if request.method == 'POST': 
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado exitosamente')
            return redirect('pg_Login')
        else: 
            messages.error(request, 'Usuario no se registro exitosamente')
            
    singIn = ClienteForm
    return render(request, 'singin.html', {'registro': singIn})
