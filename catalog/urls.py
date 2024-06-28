from django.urls import path
from catalog.views import main
from catalog.views import about
from catalog.views import category
from catalog.views import device

urlpatterns = [
    path('main/<str:category>/<int:index>', device),
    path('main/<str:category>/', category),
    path('main/', main),
    path('about/', about)
]