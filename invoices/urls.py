""" URL information for invoicing pages """

from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('customer/<customer_id>', views.customer, name='customer'),
    path('invoice/<invoice_id>', views.invoice, name='invoice'),
]
