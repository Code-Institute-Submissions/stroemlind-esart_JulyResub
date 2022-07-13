from django.urls import path
from . import views

urlpatterns = [
    path('posters/', views.posters_all_view, name='posters'),
    path('posters/add/', views.add_poster, name='add_poster'),
    path('posters/edit/<int:id>/', views.edit_poster, name='edit_poster'),
    path(
        'posters/delete/<int:id>/',
        views.delete_poster,
        name='delete_poster'
    ),
    path(
        'posters/<int:poster_id>/',
        views.poster_detail,
        name='poster-detail'
    ),
    path('like/<int:pk>/', views.like_poster, name='poster_like'),
    path('liked_posters/', views.posters_liked, name='posters_liked'),
]
