from django.shortcuts import render, redirect, get_object_or_404
from .models import RestaurantBooking
from .forms import BookingForm


# Home page with basic info and booking option

def home(request):

    return render(request, 'home.html') 

# Function to handle creating a booking

def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm()

    return render(request, create_booking.html', {'form': form})

# Booking list view

def booking_list(request):
    bookings = RestaurantBooking.objects.all()
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})

# Booking detail view

def booking_detail(request, booking_id):
    booking = get_object_or_404(RestaurantBooking, id=booking_id)
    return render(request, 'bookings/booking_detail.html', {'booking': booking})

# Function to edit booking

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
Error handling views
"""
def custom_handler404(request, exception):
    return render(request, '404.html', status=404)  

def custom_handler500(request):
    return render(request, '500.html', status=500) 
