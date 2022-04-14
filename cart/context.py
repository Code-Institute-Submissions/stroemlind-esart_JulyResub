from django.conf import settings


def cart_contents(request):
    """
    function to make the cart intems available to all templates
    """

    bag_items = []
    total = 0
    product_count = 0

    total_cost = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'total_cost': total_cost,
    }

    return context
