from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def sign_in(request):
    return render(request, 'sign_in.html')
