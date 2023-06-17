from django import forms
from .models import Logger, Booking


class LogForm(forms.ModelForm):
    class Meta:
        model = Logger
        fields = ["name", "fname", "time_log"]


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"
