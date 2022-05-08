""" View information for for PDF creation pages """

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from profiles.models import UserProfile
from invoices.models import InvoiceCustomer, Invoice

# Create your views here.


@login_required()
def view_pdf(request, invoice_id):
    """ View to return overview of invoice """

    user = request.user
    subscriber = get_object_or_404(UserProfile, user=user)
    invoice = Invoice.objects.get(id=invoice_id)
    customer_id = invoice.customer_code_id
    customer = InvoiceCustomer.objects.get(id=customer_id)

    print(customer_id)

    context = {
        'user': user,
        'subscriber': subscriber,
        'invoice': invoice,
        'customer': customer,
    }

    return render(request, 'documents/view_pdf.html', context)
