from django.shortcuts import render, get_object_or_404

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

    context = {
        'posters': posters,
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
