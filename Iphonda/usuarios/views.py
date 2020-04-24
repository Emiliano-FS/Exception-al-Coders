from django.shortcuts import render, redirect
from django.views import View
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm,User
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *

from django.template import loader
from django.http import HttpResponse

# Create your views here.
class Login(View):
    def get(self, request):
        form = AuthenticationForm()
        context = {
            'form': form
        }
        return render(request, "login.html", context)

    def post(self, request):
        username = request.POST['username'],
        password = request.POST['password'],
        user = authenticate(request, username=username[0], password=password[0])

        if user is not None:
            print('Auth correct')
            login(request, user)
        else:
            print('Login Failed')
            print(username)
            print(password)

        form = AuthenticationForm(request.POST)
        context = {
            'form': form
        }
        return render(request, "login.html", context)

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('/login/')

class Pedidos(View):
    """docstring forPedidos."""

    def get(self,request):
        template="pedidos.html"
        lista_pedidos = Orden.objects.all()
        lista_usuarios=User.objects.all()
        context = {
            'lista_pedidos':lista_pedidos,
            'listaUsuario': lista_usuarios,
        }
        print(lista_pedidos)
        return render(request,self.template,context)

    def post(self, request):
        return HttpResponse("<h1> no debiste llegar aqui </h1>")


class Signup(View):
    def get(self, request):
        context = {
            'form': SignUpForm()
        }
        return render(request, "signup.html", context)

    def post(self, request):
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login/')

        context = {
            'form': form
        }
        return render(request, "signup.html", context)
