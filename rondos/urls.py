"""rondos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from bookings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('allauth.urls')),
    path('bookings/', views.booking_list, name='booking_list'),
    path('booking/<int:booking_id>/', views.booking_detail, name='booking_detail'),
    path('booking/create/', views.create_booking, name='create_booking'),
    path('booking/edit/<int:booking_id>/', views.edit_booking, name='edit_booking'),
]


handler404 = 'bookings.views.custom_handler404'
handler500 = 'bookings.views.custom_handler500'

