from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.utils import timezone

import stripe

from posters.models import Poster
from .models import OrderLineItem
from .forms import PosterOrderForm


def checkout(request):
    """
    The view to render the checkout form
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    client_secret = settings.CLIENT_SECRET

    if request.method == 'POST':
        poster_order_form = PosterOrderForm(request.POST)

        if poster_order_form.is_valid():
            order = poster_order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                poster = get_object_or_404(Poster, pk=id)
                total += quantity * poster.price
                order_line_item = OrderLineItem(
                    order=order,
                    poster=poster,
                    quantity=quantity
                )
                order_line_item.save()

            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency='EUR',
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, 'Your Card was Declined')

            if customer.paid:
                messages.error(request, 'You have successfully paid')
                request.session['cart'] = {}
                return redirect(reverse('home'))
            else:
                messages.error(request, 'Unable to take payment')
        else:
            print(payment_form.errors)
            messages.error(request, 'We were unable to take a payment with that card')
    else:
        # poster_order_form = PosterOrderForm()
        cart = request.session.get('cart', {})

        if not cart:
            messages.error(request, "There is nothing in your shopping cart at this moment")
            return redirect(reverse('posters'))

    poster_order_form = PosterOrderForm()
    template = 'checkout/checkout.html'

    context = {
        'poster_order_form': poster_order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': client_secret,
    }

    return render(request, template, context)
