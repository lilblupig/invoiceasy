""" View information for base public pages """

from django.shortcuts import render


def index(request):
    """ View to return index page """
    return render(request, 'home/index.html')


def about(request):
    """ View to return about page """
    return render(request, 'home/about.html')
