from django.shortcuts import render, redirect
from django.contrib import messages

from .models import NewsletterSubscriber, RequestPoster
from .forms import NewsletterForm, RequestPosterForm


def index(request):
    """
    A view to render the index page
    """

    form = RequestPosterForm(request.POST)
    context = {}

    if request.method == 'POST':
        form = RequestPosterForm(request.POST)
        if form.is_valid():
            poster_request = form.save(commit=False)
            full_name = form.cleaned_data.get('full_name')
            email = form.cleaned_data.get('email')
            phone_number = form.cleaned_data.get('phone_number')
            motive = form.cleaned_data.get('motive')
            image = form.cleaned_data.get('image')
            poster_request = RequestPoster.objects.create(
                                 full_name=full_name,
                                 email=email,
                                 phone_number=phone_number,
                                 motive=motive,
                                 image=image,
                                 )
            poster_request.save()
            print(poster_request)
            messages.success(
                request,
                'Your request have been send to Us.  \
                We will get back to you shortly!'
            )
            return redirect('home')
        else:
            form = RequestPosterForm()

    template = 'home/index.html'
    context['form'] = form
    return render(request, template, context)


def about_us(request):
    """
    A view to render the About Us page
    """
    return render(request, 'home/about-us.html')


def terms_and_conditions(request):
    """
    A view to render the About Us page
    """
    return render(request, 'home/terms-and-conditions.html')


def newsletter_signup(request):
    """
    A view to render the newsletter subcription form
    """

    if request.method == 'POST':
        newsletter_form = NewsletterForm(request.POST)
        if newsletter_form.is_valid():
            instance = newsletter_form.save(commit=False)
            if NewsletterSubscriber.objects.filter(
                email=instance.email
            ).exists():
                messages.error(
                    request,
                    'Sorry, that email does already exist  \
                    as a subscriber!'
                )
            else:
                instance.save()
                messages.success(
                    request,
                    'You are now added  \
                    to the Newsletter Subscription'
                )
                return redirect('home')
        else:
            newsletter_form = NewsletterForm()

    return redirect(request.META.get('HTTP_REFERER'))
