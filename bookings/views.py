from django.shortcuts import render
from .models import RestaurantBooking
from .forms import BookingForm

# Create your views here.
"""
function to handle booking creation and redirect to 
"""
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_list')  # Redirect after saving
    else:
        form = BookingForm()

    return render(request, 'bookings/create_booking.html', {'form': form})

def booking_list(request):
    bookings = RestaurantBooking.objects.all()
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})

def booking_detail(request, booking_id):
    booking = get_object_or_404(RestaurantBooking, id=booking_id)
    return render(request, 'bookings/booking_detail.html', {'booking': booking})

"""
function to edit booking
"""
def edit_booking(request, booking_id):
    booking = get_object_or_404(RestaurantBooking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_detail', booking_id=booking.id)
    else:
        form = BookingForm(instance=booking)

    return render(request, 'bookings/edit_booking.html', {'form': form, 'booking': booking})





"""
Error handling 404 and 500 views
"""

def custom_handler404(request, exception):
    """
    Custom handler for 404 (Page Not Found) errors.
    """
    return render(request, '404.html', status=404)


def custom_handler500(request):
    """
    Custom handler for 500 (Internal Server Error) errors.
    """
    return render(request, '500.html', status=500)