""" URL information for for PDF creation pages """

from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_pdf, name='view_pdf'),
]
