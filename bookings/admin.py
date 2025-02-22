from django.contrib import admin
from .models import RestaurantBooking


class RestaurantBookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'booking_date', 'booking_time', 'status', 'table')  # Fields to display in the list view
    list_filter = ('status', 'booking_date')  
    search_fields = ('customer_name', 'customer_email', 'booking_date')  
    ordering = ('booking_date', 'booking_time')  


admin.site.register(RestaurantBooking, RestaurantBookingAdmin)

