from django.urls import path
from catalog.views import main
from catalog.views import about

urlpatterns = [
    path('main/', main),
    path('about/', about)
]