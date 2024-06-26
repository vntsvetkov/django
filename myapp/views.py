from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    return HttpResponse(
        """ <h1> Добро пожаловать на главную страницу myapp </h1> """
    )

def about(request):
    return HttpResponse(
        """ <h1> Добро пожаловать на страницу о нас приложения myapp </h1> """
    )