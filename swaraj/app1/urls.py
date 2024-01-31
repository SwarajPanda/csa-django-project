from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("menus/<int:pk>/", views.menu, name="menu"),
]
