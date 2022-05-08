""" View information for for PDF creation pages """

from django.shortcuts import render

# Create your views here.

def view_pdf(request):
    """ View to return index page """
    return render(request, 'documents/view_pdf.html')
