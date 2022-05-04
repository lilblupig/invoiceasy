""" URL information for invoicing pages """

from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('customer/', views.customer, name='customer'),
    path('invoice/', views.invoice, name='invoice'),
]
