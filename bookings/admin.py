from django.contrib import admin
from .models import RestaurantBooking

class RestaurantBookingAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'booking_date', 'booking_time', 'num_guests', 'status', 'table')
    list_filter = ('status', 'booking_date', 'table')
    search_fields = ('customer_name', 'customer_email')

    admin.site.register(RestaurantBooking, RestaurantBookingAdmin)
