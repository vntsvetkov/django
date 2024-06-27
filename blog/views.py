from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def main(request):
    return HttpResponse(
        """ <h1> Добро пожаловать на главную страницу blog </h1> """
    )