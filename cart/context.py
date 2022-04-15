from django.shortcuts import get_object_or_404
from posters.models import Poster


def cart_contents(request):
    """
    Function to make the cart intems available to all templates
    """

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        poster = get_object_or_404(Poster, pk=item_id)
        total += quantity * poster.price
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'poster': poster,
        })

    total_cost = total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'total_cost': total_cost,
    }

    return context
