from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RestaurantBooking(models.Model):
    PENDING = 'pending'
    APPROVED = 'approved'
    REJECTED = 'rejected'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
    ]

    customer_name = models.CharField(max_length=50)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=15)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    num_guests = models.PositiveIntegerField()
    special_requests = models.TextField(blank=True, null=True)
    baby_chair = models.BooleanField(default=False)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=PENDING,
    )
    table = models.PositiveIntegerField(default=1)  
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        """ Prevent duplicate bookings for the same table, date, and time. """
        unique_together = ('booking_date', 'booking_time', 'table') 

    def clean(self):
        """Prevent double booking for the same table at the same time."""
        existing_booking = RestaurantBooking.objects.filter(
            booking_date=self.booking_date,
            booking_time=self.booking_time,
            table=self.table
        ).exclude(pk=self.pk) 
        
        if existing_booking.exists():
            raise ValidationError("This table is already booked at the selected time.")

    def __str__(self):
        return f"{self.customer_name} - {self.booking_date} {self.booking_time} - Table {self.table}"
