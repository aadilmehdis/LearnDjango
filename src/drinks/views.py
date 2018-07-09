import random
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
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

class ContactView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, "contact.html", context)

    def post(self, request, *args, **kwargs):
        context = {}
        return render(request, "contact.html", context)

    def put(self, request, *args, **kwargs):
        context = {}
        return render(request, "contact.html", context)

class ContactTemplateView(TemplateView):
    template_name = 'contact.html'