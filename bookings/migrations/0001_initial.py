# Generated by Django 5.1.6 on 2025-02-14 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=50)),
                ('customer_email', models.EmailField(max_length=254)),
                ('customer_phone', models.CharField(max_length=15)),
                ('booking_date', models.DateField()),
                ('booking_time', models.TimeField()),
                ('num_guests', models.PositiveIntegerField()),
                ('special_requests', models.TextField(blank=True, null=True)),
                ('baby_chair', models.BooleanField(default=False)),
            ],
        ),
    ]
