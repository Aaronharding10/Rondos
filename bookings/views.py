from django.shortcuts import render

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