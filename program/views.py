from django.shortcuts import render
from django.shortcuts import render
from competitor.models import Competitor
from judge.models import Judge
from teacher.models import Teacher
def dashboard(request):
    return render(request, 'dashboard.html')

def global_search(request):
    query = request.GET.get('query', '')

    # Buscar en competidores
    competitors = Competitor.objects.filter(
        first_name__icontains=query
    ).distinct().order_by('first_name') | Competitor.objects.filter(
        last_name__icontains=query
    ).distinct().order_by('first_name')

    # Buscar en jueces
    judges = Judge.objects.filter(
        first_name__icontains=query
    ).distinct().order_by('first_name') | Judge.objects.filter(
        last_name__icontains=query
    ).distinct().order_by('first_name')

    # Buscar en profesores
    teachers = Teacher.objects.filter(
        first_name__icontains=query
    ).distinct().order_by('first_name') | Teacher.objects.filter(
        last_name__icontains=query
    ).distinct().order_by('first_name')


    return render(
        request,
        'program/global_search_results.html',
        {'competitors': competitors, 'judges': judges, 'teachers': teachers, 'query': query}
    )
