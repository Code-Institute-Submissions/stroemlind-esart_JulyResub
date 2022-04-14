from django.shortcuts import render, redirect


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
