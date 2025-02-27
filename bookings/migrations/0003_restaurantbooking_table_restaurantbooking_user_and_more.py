# Generated by Django 5.1.6 on 2025-02-24 15:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_restaurantbooking_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantbooking',
            name='table',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='restaurantbooking',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='restaurantbooking',
            unique_together={('booking_date', 'booking_time', 'table')},
        ),
    ]
