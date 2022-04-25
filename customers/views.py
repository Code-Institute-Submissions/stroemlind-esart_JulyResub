from django.shortcuts import render


def customer_profile(request):
    """
    The view to render a loged in user/customers
    order information
    """
    return render(request, 'customers/customer_page.html')
