from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("chris", views.chris, name="chris"),
    path("max", views.max, name ="max"),
    path("mel", views.mel, name ="mel")
]