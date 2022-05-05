""" URL information for subscription pages """

from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscribe, name='subscribe'),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
    path('success/', views.success),
    path('abort/', views.abort),
    path('webhook/', views.stripe_webhook),
]
