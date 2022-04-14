from django.shortcuts import render


def shopping_cart(request):
    """ A view to render the shoppingcart page and its content """
    return render(request, 'cart/shopping-cart.html')
