from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu

# Create your views here.
menus = [
    {"id": 1, "name": "All Night Canteen"},
    {"id": 2, "name": "Looters"},
    {"id": 3, "name": "TOTT"},
    {"id": 4, "name": "Pizzeria"},
    {"id": 5, "name": "Mr Idli"},
    {"id": 6, "name": "Midtown"},
]


def home(request):
    context = {"menus": menus}
    return render(request, "home.html", context)


def menu(request, pk):
    menu = Menu.objects.get(pk=pk)
    menu.description.replace("\n\r", "<br>")
    context = {"menu": menu}
    return render(request, "menu.html", context)
