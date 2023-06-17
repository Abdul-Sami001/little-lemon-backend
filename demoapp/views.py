from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from demoapp.forms import ApplicationForm


def form_view(request):
    form = ApplicationForm
    context = {"form": form}
    return render(request, "home.html", context)


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
