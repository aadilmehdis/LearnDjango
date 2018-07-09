from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from .models import DrinkInfo

# Create your views here. 

def drink_listview(request):
    template_name = 'drinks/drink_list.html'
    query_set = DrinkInfo.objects.all()
    context = {
        "object_list" : query_set
    }
    return render(request, template_name, context)