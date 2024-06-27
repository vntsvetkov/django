from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, HttpResponsePermanentRedirect


# Create your views here.
def main(request: HttpRequest):
    return HttpResponse(
        content=""" <h1> Добро пожаловать на главную страницу catalog </h1> """
    )


def about(request: HttpRequest):
    return HttpResponse(
        content=""" <h1> Добро пожаловать на страницу о нас приложения catalog </h1> """
    )


def redirect(request: HttpRequest):
    return HttpResponseRedirect('/catalog/main/')
