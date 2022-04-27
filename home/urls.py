from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us/', views.about_us, name='about-us'),
    path('newsletter/', views.newsletter_signup, name='newsletter_signup'),
]
