""" URL information for base public pages """

from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
]
