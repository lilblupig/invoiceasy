""" URL information for contact page """

from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
]
