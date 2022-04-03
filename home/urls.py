""" URL information for the base public pages """

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home')
]
