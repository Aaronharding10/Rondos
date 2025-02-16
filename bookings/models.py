from django.db import models
from django.contrib.auth.models import User

# Create your models here.

"""
model for bookings, to prevent double bookings and checks past bookings
"""

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
        default=PENDING,  # Default status is 'pending'
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta : 
        unique_together = ('booking_date', 'booking_time', 'table')

    def clean(self): 

        existing_booking = RestaurantBooking.objects.filter(
            booking_date=self.booking.date,
            booking_time=self.booking.time,
            table=self.table
        ).exclude(id=self.id)

        if existing_booking.exists():
            raise ValidationError("Unfortunately this table is already booked at the time selected")
        



    def __str__(self):
        return f"{self.customer_name} - {self.booking_date} - {self.status}"