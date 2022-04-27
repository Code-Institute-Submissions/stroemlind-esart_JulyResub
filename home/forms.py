from django import forms
from .models import NewsletterSubscriber


class NewsletterForm(forms.ModelForm):
    """
    Form to collect email when user wants to
    subscribe to the newsletter
    """
    class Meta:
        """
        Tells django which lines to use from the model
        """
        model = NewsletterSubscriber
        fields = ('email',)
