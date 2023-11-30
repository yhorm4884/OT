from django.shortcuts import render
from competitor.models import Competitor

def show_competitors(request):
    competitors = Competitor.objects.all()
    return render(request, 'accounts/all_account', {'all_competitors':competitors})
