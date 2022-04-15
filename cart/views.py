from django.shortcuts import render, redirect, reverse


def shopping_cart(request):
    """ A view to render the shoppingcart page and its content """
    return render(request, 'cart/shopping-cart.html')


def add_to_cart(request, item_id):
    """ View to add a specific product to the cart"""

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def remove_from_cart(request, item_id):
    """ Remove the item from the shopping cart """

    cart = request.session.get('cart', {})
    quantity = cart[item_id] - 1

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)
    request.session['cart'] = cart

    if not cart:
        return redirect(reverse('home'))
    return redirect(reverse('shopping_cart'))
