from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    """
    Customized form for Customer to update
    their information
    """
    class Meta:
        """
        Tells Django which field to exclude from the form
        """
        model = Customer
        exclude = ('customer',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'defualt_email': 'Email',
            'default_phone_number': 'Phone Number',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_county': 'County, State or Locality',
            'default_country': 'Country',
        }

        self.fields['defualt_email'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'customer-form-input'
            self.fields[field].label = False
