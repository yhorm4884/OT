from django.shortcuts import render
from competitor.models import Competitor

def show_competitors(request):
    competitor = Competitor.objects.all()
    return render(request, 'competitor/all_accounts.html', {'all_competitors':competitor})
