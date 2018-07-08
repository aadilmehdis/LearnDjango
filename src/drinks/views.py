from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#function based views
def home(request):
    return HttpResponse("Hello")