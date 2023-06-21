from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from demoapp.forms import LogForm, BookingForm


def about(request):
    return render(request, "about.html")


def form_view(request):
    form = LogForm()
    if request.method == "POST":
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "home.html", context)


def reservation(request):
    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    content = {"form": form}
    return render(request, "reservation.html", content)


def main(request, name):
    persons = {
        "ali": "male",
        "mehmet": "male",
        "selim": "female",
        "selim2": "female",
        "selim3": "female",
        "selim4": "female",
    }
    return HttpResponse("<h2>" + persons[name] + "</h2>")
    # return HttpResponse("welmoce to the home page.")
