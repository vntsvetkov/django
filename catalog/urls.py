from django.urls import path
from catalog.views import main
from catalog.views import about
from catalog.views import get_by_genre

urlpatterns = [
    path('main/', main),
    path('about/', about),
    path('<str:genre>/', get_by_genre),
]
