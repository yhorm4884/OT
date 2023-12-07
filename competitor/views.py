from django.shortcuts import render, get_object_or_404
from competitor.models import Competitor
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings

def show_competitors(request):
    competitors = Competitor.objects.all()

    # Obtener parámetros opcionales del request
    query = request.GET.get('query', '')

    # Verificar si la consulta está vacía
    if query:
        # Aplicar filtros si se proporciona un valor en el campo de búsqueda
        competitors = competitors.filter(
            first_name__icontains=query
        ) | competitors.filter(
            last_name__icontains=query
        ) | competitors.filter(
            city__icontains=query
        ) | competitors.filter(
            music_styles__name__icontains=query
        )

    # Ordenar competidores por algún campo, por ejemplo, por first_name
    competitors = competitors.order_by('first_name')

    # Eliminar duplicados
    competitors = competitors.distinct()

    # Configuración del paginador global
    paginator = Paginator(competitors, settings.GLOBAL_PAGINATION_SIZE)
    page = request.GET.get('page')

    try:
        competitors = paginator.page(page)
    except PageNotAnInteger:
        # Si la página no es un número, mostrar la primera página
        competitors = paginator.page(1)
    except EmptyPage:
        # Si la página está fuera de rango, mostrar la última página
        competitors = paginator.page(paginator.num_pages)

    # Migas de pan globales
    breadcrumbs = [
        {'label': 'Competitors', 'url': '/competitors/'},
    ]

    return render(request, 'competitor/all_accounts.html', {'competitors': competitors, 'breadcrumbs': breadcrumbs})


def competitor_detail(request, competitor_slug):
    competitor = get_object_or_404(Competitor, slug=competitor_slug)

    # Migas de pan globales
    breadcrumbs = [
        {'label': 'Competitors', 'url': '/competitors/'},
        {'label': competitor.first_name, 'url': f'/competitors/{competitor_slug}'},
    ]

    return render(request, 'competitor/competitor_detail.html', {'competitor': competitor, 'breadcrumbs': breadcrumbs})
