from home.forms import NewsletterForm


def subscription_form(request):
    """
    Context processor to render the form on
    every page of the application
    """
    form = NewsletterForm()
    context = {
        'subscription_form': form
    }

    return context
