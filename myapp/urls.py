from django.urls import path
from myapp.views import main
from myapp.views import about

urlpatterns = [
    path('main/', main),
    path('about/', about)
]