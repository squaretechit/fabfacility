from cProfile import label
from dataclasses import field
from django import forms

from .models import SubscriptionEmail


class SubscripForm(forms.ModelForm):

    class Meta:
        model = SubscriptionEmail
        fields = ['email',]
        labels = {
            'email': "Email Address"
        }
        widgets = {
            'email': forms.EmailInput(
                attrs = {
                    'placeholder' : 'Email address',
                    'class' : 'form-control',
                    'autocomplete': 'off',
                    'id': 'subscription-email'
                    }
                )
        }


class ContactForm(forms.Form):

    service_choices = [
        ('End of Lease Cleaning Melbourne','End of Lease Cleaning Melbourne'),
        ('Carpet Steam Cleaning','Carpet Steam Cleaning'),
        ('After builder Cleaning','After builder Cleaning'),
        ('Windown Cleaning','Windown Cleaning'),
        ('Oven Cleaning','Oven Cleaning'),
        ('Once-off Cleaning/Spring Clean','Once-off Cleaning/Spring Clean'),
        ('Pressure Washing','Pressure Washing'),
        ('Tile & Grout Cleaning','Tile & Grout Cleaning'),
        ('Stripping & Sealing','Stripping & Sealing'),
        ('Airbnb Cleaning Cleaning','Airbnb Cleaning Cleaning'),
        ('Carpet Steam Cleaning','Carpet Steam Cleaning'),
        ('Handyman Services','Handyman Services'),
        ('Pri-listing Cleaning','Pri-listing Cleaning'),
        ('Linens Supply','Linens Supply'),
        ('Key Delivery','Key Delivery'),
        ('24/7 Emergency Service','24/7 Emergency Service'),
        ('Real Estate Agent','Real Estate Agent'),
        ('CAirbnb/ Short Stay Management','CAirbnb/ Short Stay Management'),
        ('Commercial/Office Cleaning','Commercial/Office Cleaning'),
        ('Property Maintenance','Property Maintenance')
    ]

    name = forms.CharField(
        label='Name',
        max_length=70,
        error_messages={'required': 'Name required.'},
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Full Name'
            }
        )
    )

    email = forms.EmailField(
        label='Email',
        max_length=70,
        error_messages={'required': 'Email required.'},
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email Address'
            }
        )
    )

    phone = forms.CharField(
        label='Phone Number',
        max_length=20,
        error_messages={'required': 'Phone Number required'},
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number'
            }
        )
    )

    service = forms.CharField(
        label='Please select your service',
        error_messages={'required': 'Service required'},
        widget=forms.Select(
            choices=service_choices,
            attrs={
                'class': 'form-select',
                'aria-label': 'Please select your service'
            }
        )
    )

    message = forms.CharField(
        label='Your Message Here',
        max_length=500,
        error_messages={'required': 'Please, leave us a message.'},
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Please, leave us a message.'
            }
        )
    )
