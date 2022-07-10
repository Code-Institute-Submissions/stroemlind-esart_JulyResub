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

        widgets = {
                'name': forms.TextInput(attrs={
                    'class': 'form-control poster-form mb-2',
                    'placeholder': 'Enter Poster Name Here',
                    'aria-label': 'Enter Poster Name',
                }),
                'motive': forms.Select(attrs={
                    'class': 'form-control poster-form mb-2',
                }),
                'description': forms.Textarea(attrs={
                    'class': 'form-control poster-form mb-2',
                    'placeholder': 'Enter Poster Description Here',
                    'aria-label': 'Enter Poster Description',
                }),
                'size': forms.NullBooleanSelect(attrs={
                    'class': 'form-control poster-form mb-2',
                    'placeholder': 'Select Size',
                    'aria-label': 'Select Size',
                }),
                'quantity': forms.NumberInput(attrs={
                    'class': 'form-control poster-form mb-2',
                    'placeholder': 'Enter Quantity',
                    'aria-label': 'Enter Quantity',
                }),
                'price': forms.NumberInput(attrs={
                    'class': 'form-control poster-form mb-2',
                    'placeholder': 'Enter Price Here',
                    'aria-label': 'Enter Price',
                }),
                'image': forms.FileInput(attrs={
                    'class': 'form-control rounded-0 border-dark mb-2',
                    'placeholder': 'Enter Image Here e.g image.jpeg',
                    'aria-label': 'Enter Image',
                }),
        }
