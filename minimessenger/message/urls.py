from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('message/<str:key>/', get_secret_message),
]
