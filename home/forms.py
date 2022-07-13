from django import forms

from .models import NewsletterSubscriber, RequestPoster


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
        fields = ('news_email',)

        widgets = {
            'news_email': forms.EmailInput(attrs={
                'class': 'newsletter-style form-control',
                'placeholder': 'Enter email here',
                'aria-label': 'Signup for newsletter',
            }),
        }

        labels = {
            'news_email': '',
        }


class RequestPosterForm(forms.ModelForm):
    """
    The Form model to collect information
    from user who wants to order a customized
    poster
    """
    class Meta:
        """
        Tells django which lines to use from the model
        """
        model = RequestPoster
        fields = (
            'full_name',
            'email',
            'phone_number',
            'motive',
            'image',
        )

        widgets = {
                'full_name': forms.TextInput(attrs={
                    'class': 'form-control request-form mb-2',
                    'placeholder': 'Enter Your Full Name Here',
                    'aria-label': 'Enter Full Name',
                }),
                'email': forms.EmailInput(attrs={
                    'class': 'form-control request-form mb-2',
                    'placeholder': 'Enter Your Email here',
                    'aria-label': 'Enter Email',
                }),
                'phone_number': forms.NumberInput(attrs={
                    'class': 'form-control request-form mb-2',
                    'placeholder': 'Enter Your Phone number here',
                    'aria-label': 'Enter Phone number',
                }),
                'motive': forms.TextInput(attrs={
                    'class': 'form-control request-form mb-2',
                    'placeholder': 'Enter Description/Motive of Poster here',
                    'aria-label': 'Enter Motive Request',
                }),
                'image': forms.FileInput(attrs={
                    'class': 'form-control rounded-0 border-dark mb-2',
                }),
        }
