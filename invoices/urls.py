""" URL information for invoicing pages """

from django.urls import path
from . import views

urlpatterns = [
    path('', views.invoices, name='invoices'),
    path('customer/', views.customer, name='customer'),
    path('invoice/', views.invoice, name='invoice'),
]
