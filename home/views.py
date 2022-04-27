from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponseRedirect
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
    A view to render the newsletter subcribtion form
    """
    newsletter_form = NewsletterForm(request.POST)
    newsletter = get_object_or_404(NewsletterSubscriber)

    if request.method == 'POST':
        if newsletter_form.is_valid():
            instance = newsletter_form.save(commit=False)
            if NewsletterSubscriber.objects.filter(email=instance.email).exists():
                messages.error(
                    request,
                    f'Sorry, {newsletter.email} does already exist'
                    f'as a subscriber!'
                )
            else:
                instance.save()
                messages.success(
                    request,
                    'You are now added'
                    'to the Newsletter Subscribtion'
                )
                return HttpResponseRedirect(reverse('home'))
        else:
            newsletter_form = NewsletterForm()

    template = 'home/index.html'
    context = {
        'newsletter_form': newsletter_form,
    }

    return render(request, template, context)
