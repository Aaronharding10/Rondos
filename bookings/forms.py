from django import forms
from .models import RestaurantBooking
from django.core.validators import MinValueValidator

class BookingForm(forms.ModelForm):

    """
    A form for creating or updating restaurant booking. The form makes sure that the minimum
    number of guests is1 and provides options for special requests etc.
    """

    num_guests = forms.IntegerField(validators=[MinValueValidator(1)])
    special_requests = forms.CharField(
        widget=forms.Textarea(attrs={'rows' : 3}),
        required=False
    )

class Meta : 
    model = RestaurantBooking
    fields = [
        'customer_name', 
            'customer_email', 
            'customer_phone', 
            'booking_date', 
            'booking_time', 
            'num_guests', 
            'table', 
            'special_requests', 
            'baby_chair'
    ]

    widgets = {
        'booking_date': forms.DateInput(attrs={'type': 'date'}),
        'booking_time': forms.TimeInput(attrs={'type': 'time'}),
        }