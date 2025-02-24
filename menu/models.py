from django.db import models
from cloudinary.models import CloudinaryField

class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('main', 'Main Course'),
        ('dessert', 'Dessert'),
        ('drink', 'Drink'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    image = CloudinaryField('menu_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} - €{self.price}"
