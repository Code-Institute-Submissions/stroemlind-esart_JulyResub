from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q

from cart.context import cart_contents
from .models import Poster, Motive


def posters_all_view(request):
    """ A view to render the Poster product page """

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
    """ A view to show individual poster details """

    poster = get_object_or_404(Poster, pk=poster_id)
    cart = cart_contents(request)
    template = 'posters/poster-detail.html'
    liked = False

    if request.method == 'POST':
        if poster.like.filter(id=poster.request.user.id).exists():
            liked = True
            return

    context = {
        'poster': poster,
        'cart': cart,
        'liked': liked,
    }

    return render(request, template, context)


class PosterLikeView(View):
    """
    The view for likes
    """
    def poster(self, request, pk, *args, **kwargs):
        """
        The function to determine the view if a user has liked a post or not
        """
        poster = get_object_or_404(Poster, pk=pk)
        if poster.like.filter(id=request.user.id).exists():
            poster.like.remove(request.user)
        else:
            poster.like.add(request.user)

        return HttpResponseRedirect(reverse('posters', args=[pk]))


# class LikedPosters(generic.ListView):
#     """
#     The function for the 'Most Populare Post' view
#     """
#     model = Poster
#     queryset = Poster.objects.filter(status=1).annotate(
#         like_count=Count('likes')).order_by('-like_count')
#     template_name = 'liked_posters.html'
