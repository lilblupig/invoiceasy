""" URL information for product and pricing pages """

from django.urls import path
from . import views

urlpatterns = [
    path('', views.pricing, name='pricing'),
    path('<plan_id>', views.plan_detail, name='plan_detail'),
]
