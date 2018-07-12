from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from .models import DrinkInfo

# Create your views here. 

def drink_listview(request):
    template_name = 'drinks/drink_list.html'
    query_set = DrinkInfo.objects.all()
    context = {
        "object_list" : query_set
    }
    return render(request, template_name, context)

class DrinkListView(ListView):
    # template_name = 'drinks/drink_list.html'
    def get_queryset(self):
        place_of_origin = self.kwargs.get("place_of_origin")
        if place_of_origin:
            queryset = DrinkInfo.objects.filter(
                Q(place_of_origin__iexact=place_of_origin) |
                Q(place_of_origin__icontains=place_of_origin)
            )
        else:
            queryset = None
        return queryset

class DrinkDetailView(DetailView):
    queryset = DrinkInfo.objects.all()

    def get_context_data(self, *args, **kwargs):
        print(self.kwargs)
        context = super(DrinkDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    def get_object(self, *args, **kwargs):
        drink_id = self.kwargs.get("drink_id")
        obj = get_object_or_404(DrinkInfo, id=drink_id) # pk = drink_id
        return obj


