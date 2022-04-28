from django.urls import path
from . import views

urlpatterns = [
    path('posters/', views.posters_all_view, name='posters'),
    path(
        'posters/<int:poster_id>/',
        views.poster_detail,
        name='poster-detail'
    ),
    path('like/<int:pk>', views.PosterLikeView.as_view(), name='poster_like'),
]
