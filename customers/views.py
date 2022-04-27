from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import Customer
from .forms import CustomerForm

from checkout.models import Order


def customer_profile(request):
    """
    The view to render a logged in user/customers
    order information
    """
    customer = get_object_or_404(Customer, customer=request.user)

    if request.method == 'POST':
        customer_form = CustomerForm(request.POST, instance=customer)
        if customer_form.is_valid():
            customer_form.save()
            messages.success(request, 'Information updated successfully!')

    customer_form = CustomerForm(instance=customer)
    orders = customer.orders.all()

    template = 'customers/customer_page.html'
    context = {
        'customer_form': customer_form,
        'orders': orders,
        'on_customer_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    """
    View to render Customers Order History
    """

    order = get_object_or_404(Order, order_number=order_number)

    template = 'checkout/success_checkout.html'
    context = {
        'order': order,
        'from_customer': True,
    }

    return render(request, template, context)
