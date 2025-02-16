from django import forms
from .models import RestaurantBooking
from django.core.validators import MinValueValidator

class BookingForm(forms.ModelForm):
    """
    A form for creating or updating a restaurant booking.
    The form ensures that the minimum number of guests is at least 1 and provides options for special requests, etc.
    """
    num_guests = forms.IntegerField(validators=[MinValueValidator(1)], required=True)
    special_requests = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}),
        required=False
    )

    class Meta:
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
            'baby_chair',
        ]
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'}),
            'booking_time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean(self):
        """
        This method makes sure the number of guests is at least 1 and checks that the table is not double-booked.
        """
        cleaned_data = super().clean()
        num_guests = cleaned_data.get('num_guests')


        if num_guests and num_guests < 1:
            raise forms.ValidationError("Number of guests must be at least 1")

        
        booking_date = cleaned_data.get('booking_date')
        booking_time = cleaned_data.get('booking_time')
        table = cleaned_data.get('table')

       
        existing_booking = RestaurantBooking.objects.filter(
            booking_date=booking_date,
            booking_time=booking_time,
            table=table
        )

        if existing_booking.exists():
            raise forms.ValidationError("This table is already booked at the selected time.")

        return cleaned_data
