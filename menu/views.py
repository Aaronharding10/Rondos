from django.shortcuts import render
from .models import MenuItem

def menu_list(request):
    menu_items = MenuItem.objects.all()
    return render (request, 'menu/menu_list.html', {'menu_items' : menu_items})

# Create your views here.
