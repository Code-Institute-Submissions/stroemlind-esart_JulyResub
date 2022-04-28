from django.shortcuts import render, redirect
from django.contrib import messages

from .models import NewsletterSubscriber
from .forms import NewsletterForm


def index(request):
    """ A view to render the index page """
    return render(request, 'home/index.html')


def about_us(request):
    """ A view to render the About Us page """
    return render(request, 'home/about-us.html')


def newsletter_signup(request):
    """
    A view to render the newsletter subcription form
    """

    if request.method == 'POST':
        newsletter_form = NewsletterForm(request.POST)
        if newsletter_form.is_valid():
            instance = newsletter_form.save(commit=False)
            if NewsletterSubscriber.objects.filter(email=instance.email).exists():
                messages.error(
                    request,
                    'Sorry, that email does already exist'
                    'as a subscriber!'
                )
            else:
                instance.save()
                messages.success(
                    request,
                    'You are now added'
                    'to the Newsletter Subscription'
                )
                return redirect('home')
        else:
            newsletter_form = NewsletterForm()

    return redirect(request.META.get('HTTP_REFERER'))
