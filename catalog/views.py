from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, HttpResponseNotFound


# Create your views here.
def main(request: HttpRequest):
    return HttpResponse(
        content=""" <h1> Добро пожаловать в catalog электронной библиотеки </h1> """
    )


def get_by_genre(request: HttpRequest, genre=None):
    data = ['classic', 'adventure', 'fantastic']
    if genre in data:
        title = request.GET.get('title', '')
        author = request.GET.get('author', '')

        if not title and not author:
            return HttpResponseNotFound(f""" <h1> В жанре {genre} этой книги не найдено </h1>""")

        # Запрос к БД по 2 параметрам
        # Посмотреть что пришли непустые данные

        return HttpResponse(
            content=f""" 
            <h1> Страница с книгами в жанре {genre} </h1>
            <p> Название: {title} </p>
            <p> Автор: {author} </p> 
            """
        )
    else:
        return HttpResponseNotFound(f""" <h1> В жанре {genre} книг не найдено </h1>""")


def about(request: HttpRequest):
    return HttpResponse(
        content=""" <h1> Добро пожаловать на страницу о нас приложения catalog </h1> """
    )


# def category(request: HttpRequest, category=None):
#     if category not in ('phones', 'laptop'):
#         return HttpResponse(
#             content=f""" <h1> Категория {category} не найдена </h1> """
#         )
#     device_name = request.GET.get('device_name')
#     model = request.GET.get('model')
#
#     return HttpResponse(
#         content=f"""
#         <h1> Добро пожаловать на страницу {category} нашего catalog </h1>
#         <p>Нзвание устройства: {device_name}</p>
#         <p>Модель: {model}</p>
#         """
#     )
#
#
# def device(request: HttpRequest, category=None, index=None):
#     if index not in (123456, 123457):
#         return HttpResponse(
#             content=f""" <h1> Устройство {index} в категории {category} не найдено </h1> """
#         )
#
#     return HttpResponse(
#         content=f""" <h1> Добро пожаловать на страницу устройства №{index} нашего catalog </h1> """
#     )
#
#
#
#
# def redirect(request: HttpRequest):
#     return HttpResponseRedirect('/catalog/main/')
