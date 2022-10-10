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

    else:
        return render(request, "transportation/index.html")

def protransit(request):
    pass 



