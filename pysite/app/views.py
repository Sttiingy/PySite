from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def login(request):
    return render(request, "app/login.html")