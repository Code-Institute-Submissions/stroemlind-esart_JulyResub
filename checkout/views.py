from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.utils import timezone

import stripe

from posters.models import Poster
from cart.context import cart_contents
from .models import OrderLineItem
from .forms import PosterOrderForm


def checkout(request):
    """
    The view to render the checkout form
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    client_secret = settings.CLIENT_SECRET

    cart = request.session.get('cart', {})

    if not cart:
        messages.error(request, "There is nothing in your shopping cart at this moment")
        return redirect(reverse('posters'))

    current_cart = cart_contents(request)
    total = current_cart['total_cost']
    amount_total = round(total * 100)
    stripe_currency = 'EUR'
    stripe.api_key = client_secret
    intent = stripe.PaymentIntent.create(
        amount=amount_total,
        currency=stripe_currency,
    )

    print(intent)

    poster_order_form = PosterOrderForm()
    template = 'checkout/checkout.html'

    context = {
        'poster_order_form': poster_order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
