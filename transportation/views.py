from unittest import result
from django.shortcuts import render
from .models import Transportation, Politician


def index(request):
    if 'Washington' in request.POST:
        results = Politician.objects.filter(state = 'Washington')
        return render(request, "transportation/state.html", {'results': results, 'state': 'Washington', })
    elif 'Hawaii' in request.POST:
        results = Politician.objects.filter(state = 'Hawaii')
        return render(request, "transportation/state.html", {'results': results})
    else:
        return render(request, "transportation/index.html")

def protransit(request):
    pass 



