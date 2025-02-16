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
