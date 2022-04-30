from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.contrib import messages
from django.db.models import Q

from cart.context import cart_contents
from .models import Poster, Motive


def posters_all_view(request):
    """
    A view to render the Poster product page
    """

    posters = Poster.objects.all()
    template = 'posters/posters-page.html'
    query = None
    motives = None

    if request.GET:
        if 'motive' in request.GET:
            motives = request.GET['motive'].split(',')
            posters = posters.filter(motive__name__in=motives)
            motives = Motive.objects.filter(name__in=motives)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request,
                    "You need to enter something to search for"
                )
                return redirect(reverse('posters'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            posters = posters.filter(queries)

    context = {
        'posters': posters,
        'search': query,
        'motives_atm': motives,
    }

    return render(request, template, context)


def poster_detail(request, poster_id):
    """
    A view to show individual poster details
    """

    poster = get_object_or_404(Poster, pk=poster_id)
    cart = cart_contents(request)
    template = 'posters/poster-detail.html'
    liked = False

    if poster.like.filter(id=request.user.id).exists():
        liked = True

    context = {
        'poster': poster,
        'cart': cart,
        'liked': liked,
    }

    return render(request, template, context)


def like_poster(request, pk):
    """
    The function to determine the view if a user has liked a post or not
    """
    poster = get_object_or_404(Poster, pk=pk)

    if poster.like.filter(id=request.user.id).exists():
        poster.like.remove(request.user)
    else:
        poster.like.add(request.user)

    return redirect(reverse('poster-detail', args=[pk]))


def posters_liked(request):
    """
    The function to determine the view if a user has liked a post or not
    """
    # poster = get_object_or_404(Poster)

    # if poster.like.filter(id=request.user.id).exists():
    likes = Poster.objects.get(pk=1).like.all()

    template = 'posters/liked_posters.html'
    context = {
        'likes': likes,
    }

    return render(request, template, context)

    # poster = get_object_or_404(Poster, pk=pk)

    # if poster.like.filter(pk=request.user.pk).exists():
    #     poster.like.remove(request.user)
    # else:
    #     poster.like.add(request.user)

    # return redirect(request.META.get('HTTP_REFERER'))

     # posters = get_object_or_404(Poster, like=request.user)

    # if request.user.is_authenticated:
    #     likes = Poster.objects.filter(like=posters)

    # poster = get_object_or_404(Poster, pk=pk)
    # liked = False

    # if poster.like.filter(id=like.request.user.id).exists():
    #     liked = True
