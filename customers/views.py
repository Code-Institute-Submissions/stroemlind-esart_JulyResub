from django.shortcuts import render, get_object_or_404

from .models import Customer
from .forms import CustomerForm

from checkout.models import Order


def customer_profile(request):
    """
    The view to render a logged in user/customers
    order information
    """
    customer = get_object_or_404(Customer, customer=request.user)

    customer_form = CustomerForm(instance=customer)
    orders = customer.orders.all()

    template = 'customers/customer_page.html'
    context = {
        'customer_form': customer_form,
        'orders': orders,
    }

    return render(request, template, context)
