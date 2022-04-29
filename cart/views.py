from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from posters.models import Poster


def shopping_cart(request):
    """ A view to render the shoppingcart page and its content """
    return render(request, 'cart/shopping-cart.html')


def add_to_cart(request, item_id):
    """ View to add a specific product to the cart"""
    poster = get_object_or_404(Poster, pk=item_id)

    # quantity = int(request.POST.get('quantity'))
    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] = quantity
        messages.error(
            request,
            f'{poster.name} is already in the bag'
        )
    else:
        cart[item_id] = quantity
        messages.success(
            request,
            f'{poster.name} was added to the shopping cart'
        )

    request.session['cart'] = cart
    return redirect(redirect_url)


def remove_from_cart(request, item_id):
    """ Remove the item from the shopping cart """

    poster = get_object_or_404(Poster, pk=item_id)
    cart = request.session.get('cart', {})
    quantity = cart[item_id] - 1

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)
    request.session['cart'] = cart
    messages.success(
            request,
            f'{poster.name} was removed from the shopping cart'
        )

    if not cart:
        return redirect(reverse('home'))
    return redirect(reverse('shopping_cart'))
