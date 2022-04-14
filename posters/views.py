from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q

from .models import Poster, Motive


def index(request):
    """ A view to render the index page """
    return render(request, 'index.html')


def about_us(request):
    """ A view to render the About Us page """
    return render(request, 'about-us.html')


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
    template = 'posters/poster-detail.html'

    context = {
        'poster': poster,
    }

    return render(request, template, context)

# class LikeView(View):
#     """
#     The view for likes
#     """
#     def post(self, request, pk, *args, **kwargs):
#         """
#         The function to determine the view if a user has liked a post or not
#         """
#         post = get_object_or_404(Post, pk=pk)
#         if post.likes.filter(id=request.user.id).exists():
#             post.likes.remove(request.user)
#         else:
#             post.likes.add(request.user)

#         return HttpResponseRedirect(reverse('post-detail', args=[pk]))
