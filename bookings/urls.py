from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking_list, name='booking_list'),
    path('create/', views.create_booking, name='create_booking'),
    path('<int:booking_id>/', views.booking_detail, name='booking_detail'),
    path('<int:booking_id>/edit/', views.edit_booking, name='edit_booking'),
]

