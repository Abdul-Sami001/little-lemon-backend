from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("home/", views.form_view),
    path("reservation", views.reservation),
]
