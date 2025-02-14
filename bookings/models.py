from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class RestaurantBooking(models.model) : 
    customer_name = models.CharField(max_length=50)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=15)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    num_guests = models.PositiveIntegerField()
    special_requests = models.TextField()
    baby_chair = models.BooleanField(default=false)

    def __str__(self) : 
        return f"{self.customer_name} - {self.booking_date}"
    

