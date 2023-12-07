from django.shortcuts import render, get_object_or_404
from judge.models import Judge
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings

def show_judges(request):
    judges = Judge.objects.all()

    # Obtener parámetros opcionales del request
    query = request.GET.get('query', '')

    # Verificar si la consulta está vacía
    if query:
        # Aplicar filtros si se proporciona un valor en el campo de búsqueda
        judges = judges.filter(
            first_name__icontains=query
        ) | judges.filter(
            last_name__icontains=query
        ) | judges.filter(
            job__icontains=query
        )

    # Ordenar jueces por algún campo, por ejemplo, por first_name
    judges = judges.order_by('first_name')

    # Configuración del paginador global
    paginator = Paginator(judges, settings.GLOBAL_PAGINATION_SIZE)
    page = request.GET.get('page')

    try:
        judges = paginator.page(page)
    except PageNotAnInteger:
        # Si la página no es un número, mostrar la primera página
        judges = paginator.page(1)
    except EmptyPage:
        # Si la página está fuera de rango, mostrar la última página
        judges = paginator.page(paginator.num_pages)

    # Migas de pan globales
    breadcrumbs = [
        {'label': 'Judges', 'url': '/judges/'},
    ]

    return render(request, 'judge/all_judges.html', {'judges': judges, 'breadcrumbs': breadcrumbs})
def judge_detail(request, judge_slug):
    judge = get_object_or_404(Judge, slug=judge_slug)

    # Migas de pan globales
    breadcrumbs = [
        {'label': 'Judges', 'url': '/judges/'},
        {'label': judge.first_name, 'url': f'/judges/{judge_slug}/'},
    ]

    return render(request, 'judge/judge_detail.html', {'judge': judge, 'breadcrumbs': breadcrumbs})