from django.shortcuts import render, redirect, reverse, get_object_or_404

from .models import Poster, Motive

# Create your views here.
def index(request):
    """ A view to render the index page """
    return render(request, 'index.html')


def about_us(request):
    """ A view to render the About Us page """
    return render(request, 'about-us.html')


def posters(request):
    """ A view to render the Poster product page """

    posters = Poster.objects.all()
    template = 'posters/posters-page.html'

    context = {
        'posters': posters,
    }

    return render(request, template, context)
