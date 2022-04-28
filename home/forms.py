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

        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'newsletter-style form-control',
                'label': 'hidden',
                'placeholder': 'Enter email here',
            }),
        }

        labels = {
            'email': '',
        }

        # def __init__(self, *args, **kwargs):
        #     """
        #     Add placeholders and classes, remove auto-generated
        #     labels and set autofocus on first field
        #     """
        #     super().__init__(*args, **kwargs)
        #     placeholders = {
        #         'email': 'Enter email here',
        #     }

        #     for field in self.fields:
        #         placeholder = placeholders[field]
        #         self.fields[field].widget.attrs['placeholder'] = placeholder
        #         self.fields[field].widget.attrs['class'] = (
        #             'newsletter-style',
        #             'form-control'
        #         )
        #         self.fields[field].label = False
