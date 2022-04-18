from django.shortcuts import render


def index(request):
    """ A view to render the index page """
    return render(request, 'home/index.html')


def about_us(request):
    """ A view to render the About Us page """
    return render(request, 'home/about-us.html')
