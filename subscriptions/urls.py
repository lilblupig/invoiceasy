""" URL information for subscription pages """

from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscribe, name='subscribe'),
    path('config/', views.stripe_config),
]
