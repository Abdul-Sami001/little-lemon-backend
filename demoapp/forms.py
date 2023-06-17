from django import forms

CHOICES = (
    ("1", "Morning"),
    ("2", "Afternoon"),
    ("3", "Night"),
)


class ApplicationForm(forms.Form):
    name = forms.CharField(max_length=100)
    fname = forms.CharField(max_length=50)
    Shifts = forms.ChoiceField(choices=CHOICES)
    time_log = forms.TimeField()
