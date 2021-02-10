from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .models import *


# Sistema
def user_login(request):
    if request.user.is_authenticated:
        return redirect(to="mantenedor-fechas")

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(to='mantenedor-fechas')
        else:
            messages.error(request, 'Credenciales incorrectas')
    return render(request, 'app/login.html')

def logout_user(request):
    logout(request)
    return redirect(to="login")

# Administrador
def mantenedor_fecha(request):
    if not request.user.is_authenticated:
        return redirect(to='login')

    try:
        rol = Rol.objects.get(user=request.user)
        user_centro = rol.centros
        dias = user_centro.dias.all()

        # print(dias[0].horas.all())
        data = {'centros': user_centro, 'dias': dias}
        return render(request, 'app/mantenedor_fechas.html', data)
    
    except ObjectDoesNotExist:
        logout(request)
        messages.error(request, 'Usuario no tiene un centro asociado')
        return redirect(to='login')