from itertools import count
from unittest import result
from django.shortcuts import render
from .models import Transportation, Politician





def index(request):
    if 'Washington' in request.POST:

        results = Politician.objects.filter(state = 'Washington').values_list('district', flat=True).distinct()
        group_by_district = {}
        for value in results:
            group_by_district[value] = Politician.objects.filter(state = 'Washington', district = value)
        return render(request, "transportation/state.html", {'results': group_by_district, 'state': 'Washington', })

    elif 'Hawaii' in request.POST:
        results = Politician.objects.filter(state = 'Hawaii').values_list('district', flat=True).distinct()
        group_by_district = {}
        for value in results:
            group_by_district[value] = Politician.objects.filter(state = 'Hawaii', district = value)
        return render(request, "transportation/state.html", {'results': group_by_district, 'state': 'Hawaii'})

    else: # We can get each individual state and load each state into the index.html page. 
        allstates = Politician.objects.values_list('state') 
        return render(request, "transportation/index.html", {'states': allstates})

def protransit(request):
    pass 

def quotes(request, quotes_id):
    if request.method == "GET":
        person = Politician.objects.values_list('full_name', flat=True).get(pk = quotes_id)
        quotes = Transportation.objects.filter(politician__pk = quotes_id).values_list('quotes', 'website_found')
        return render(request, "transportation/viewmore.html", {"person": person, "quotes": quotes})


