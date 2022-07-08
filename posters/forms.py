from django import forms
from .models import Poster


class PosterForm(forms.ModelForm):
    """
    The PosterForm model to add
    new posters to the shop
    """
    class Meta:
        """
        Tells django which lines to use from the model
        """
        model = Poster
        exclude = ('like', )
