from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path(
        'success_checkout/<order_number>',
        views.success_checkout,
        name='success_checkout'
    ),
]
