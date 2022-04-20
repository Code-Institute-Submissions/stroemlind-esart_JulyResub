from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import PosterOrderForm

def checkout(request):
    """
    The view to render the checkout form
    """

    cart = request.session.get('cart', {})

    if not cart:
        messages.error(request, "There is nothing in your shopping cart at this moment")
        return redirect(reverse('posters'))

    poster_order_form = PosterOrderForm()
    template = 'checkout/checkout.html'

    context = {
        'poster_order_form': poster_order_form,
    }

    return render(request, template, context)
