from django.urls import path
from .views import poll_home

urlpatterns = [
    path('', poll_home, name='poll_home'),
]
