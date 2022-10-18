from itertools import count
from unittest import result
from django.shortcuts import render
from .models import Transportation, Politician


# Order by district number !!


def index(request):
    return render(request, "transportation/index.html")

def protransit(request, state_name):
    results = Politician.objects.filter(state = state_name, transportation__info_or_not = "Pro Transit").values_list('district', flat=True).distinct().order_by('district')
    group_by_district = {}
    for value in results:
        group_by_district[value] = Politician.objects.filter(state = state_name, district = value, transportation__info_or_not = "Pro Transit")
    return render(request, "transportation/protransit.html", {'results': group_by_district, 'state': state_name}) 

def state(request, state_name):
    results = Politician.objects.filter(state = state_name).values_list('district', flat=True).distinct().order_by('district')
    group_by_district = {}
    for value in results:
        group_by_district[value] = Politician.objects.filter(state = state_name, district = value)
    return render(request, "transportation/state.html", {'results': group_by_district, 'state': state_name })

def quotes(request, quotes_id):
    if request.method == "GET":
        person = Politician.objects.values_list('full_name', flat=True).get(pk = quotes_id)
        quotes = Transportation.objects.filter(politician__pk = quotes_id)
        return render(request, "transportation/viewmore.html", {"person": person, "quotes": quotes})
