import json
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from boogie.router import Router
from users.models import Medic, Clerk

app_name = 'users'
urlpatterns = Router()


@urlpatterns.route('efetuar-login/')
def sign_in(request):
    """
    [...]
    """

    if request.method == 'GET':

        if request.user.is_authenticated:
            response = redirect('/')
        else:
            response = render(request, 'sign_in.html')

        return response

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            response = redirect('/')

        else:
            messages.add_message(
                request,
                messages.ERROR,
                "Usuário e/ou senha incorreto(s).",
                extra_tags="alert alert-danger"
            )
            response = render(request, 'sign_in.html')

    return response

@urlpatterns.route('encerrar-sessao/')
def sign_out(request):
    """
    [...]
    """

    if request.method == 'GET':
        logout(request)

    response = redirect('/')

    return response
