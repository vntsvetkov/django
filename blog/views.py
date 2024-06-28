from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.http import HttpResponseRedirect


# Create your views here.
def main(request: HttpRequest):
    return HttpResponse(
        """ <h1> Добро пожаловать на главную страницу blog </h1> """
    )


def redirect(request: HttpRequest):
    return HttpResponseRedirect('/blog/main/')