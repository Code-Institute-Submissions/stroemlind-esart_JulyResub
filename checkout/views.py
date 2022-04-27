from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.utils import timezone

import stripe

from posters.models import Poster
from cart.context import cart_contents
from customers.forms import CustomerForm
from customers.models import Customer
from .models import Order, OrderLineItem
from .forms import PosterOrderForm


def checkout(request):
    """
    The view to render the checkout form
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    client_secret = settings.CLIENT_SECRET

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        poster_order_form = PosterOrderForm(request.POST)

        if poster_order_form.is_valid():
            order = poster_order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            for item_id, quantity in cart.items():
                try:
                    poster = get_object_or_404(Poster, pk=item_id)
                    # total += quantity * poster.price
                    order_line_item = OrderLineItem(
                        order=order,
                        poster=poster,
                        quantity=quantity
                    )
                    order_line_item.save()
                except Poster.DoesNotExist:
                    messages.error(request, (
                        "A product in the cart wasn't found in our database"
                        "Please contact us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('shopping_cart'))

            # Save the info to the user's profile if all is well
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('success_checkout',
                                    args=[order.order_number]))
        else:
            messages.error(request, ('There was an error with your form. '
                                     'Please double check your information.'))
    else:
        cart = request.session.get('cart', {})

        if not cart:
            messages.error(request, (
                'There is nothing in your shopping cart at this moment'))
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

    poster_order_form = PosterOrderForm()
    template = 'checkout/checkout.html'

    context = {
        'poster_order_form': poster_order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def success_checkout(request, order_number):
    """
    View handling successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        customer = Customer.objects.get(customer=request.user)
        order.customer_info = customer
        order.save()

        if save_info:
            info_data = {
                'defualt_email': order.email,
                'defualt_phone_number': order.phone_number,
                'defualt_street_address1': order.street_address1,
                'defualt_street_address2': order.street_address2,
                'defualt_postcode': order.postcode,
                'defualt_town_or_city': order.town_or_city,
                'defualt_county': order.county,
                'defualt_country': order.country,
            }
            customer_form = CustomerForm(info_data, instance=customer)
            if customer_form.is_valid():
                customer_form.save()

    messages.success(request, f'Order successfully made! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/success_checkout.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
