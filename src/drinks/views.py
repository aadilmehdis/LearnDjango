import random
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#function based views
def home(request):
    context = {
        "html_var" : "PETA MELLARK",
        "random_number" : random.randint(0, 999999999999)
    }
    return render(request, "home.html", context)

def about(request):
    context = {
    }
    return render(request, "about.html", context)

def contact(request):
    context = {
    }
    return render(request, "contact.html", context)