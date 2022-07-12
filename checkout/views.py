from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.mail import send_mail
from django.template.loader import render_to_string
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

            # Save the info to the user's profile
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

    if request.user.is_authenticated:
        try:
            customer = Customer.objects.get(customer=request.user)
            poster_order_form = PosterOrderForm(initial={
                'full_name': customer.customer.get_full_name(),
                'email': customer.defualt_email,
                'phone_number': customer.default_phone_number,
                'street_address1': customer.default_street_address1,
                'street_address2': customer.default_street_address2,
                'postcode': customer.default_postcode,
                'town_or_city': customer.default_town_or_city,
                'county': customer.default_county,
                'country': customer.default_country,
            })
        except Customer.DoesNotExist:
            poster_order_form = PosterOrderForm()
    else:
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
                'default_phone_number': order.phone_number,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_county': order.county,
                'default_country': order.country,
            }
            customer_form = CustomerForm(info_data, instance=customer)
            if customer_form.is_valid():
                customer_form.save()

    # subject = render_to_string(
    #     'checkout/confirmation_emails/confirmation_email_subject.txt',
    #     {'order': order})
    subject = f"ES Art Confirmation for Order Number {{ order.order_number }}"
    # body = render_to_string(
    #     'checkout/confirmation_emails/confirmation_email_body.txt',
    #     {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})
    body = (
        f"Hello {order.full_name }!"
        "This is a confirmation of your order at ES Art."
        "Your order information is below:"
        f"Order Number: {order.order_number}"
        f"Order Date: {order.date}"
        f"Order Total: €{order.order_total}"
        f"Delivery: €{order.delivery_cost}"
        f"Grand Total: €{order.total_cost}"
        f"If you have any questions, feel contact us at {contact_email}."
        f"Thank you for your order!"
        f"Sincerely,"
        f"ES Art"
    )

    send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [order.email]
        )

    messages.success(
        request,
        f'Order successfully made! Your order number is {order_number}.')

    if 'cart' in request.session:
        del request.session['cart']

    context = {
        'order': order,
    }

    return render(request, 'checkout/success_checkout.html', context)
