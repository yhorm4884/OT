# teacher/views.py
from django.shortcuts import render, get_object_or_404
from teacher.models import Teacher
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def show_teachers(request):
    teachers = Teacher.objects.all()

    # Obtener parámetros opcionales del request
    query = request.GET.get('query', '')

    # Verificar si la consulta está vacía
    if query:
        # Aplicar filtros si se proporciona un valor en el campo de búsqueda
        teachers = teachers.filter(
            first_name__icontains=query
        ) | teachers.filter(
            last_name__icontains=query
        ) | teachers.filter(
            subject__icontains=query
        )

    # Ordenar profesores por algún campo, por ejemplo, por first_name
    teachers = teachers.order_by('first_name')

    # Configuración del paginador
    paginator = Paginator(teachers, 8)
    page = request.GET.get('page')

    try:
        teachers = paginator.page(page)
    except PageNotAnInteger:
        # Si la página no es un número, mostrar la primera página
        teachers = paginator.page(1)
    except EmptyPage:
        # Si la página está fuera de rango, mostrar la última página
        teachers = paginator.page(paginator.num_pages)

    # Migas de pan globales
    breadcrumbs = [
        {'label': 'Profesores', 'url': '/teachers/'},
    ]

    return render(request, 'teacher/all_teachers.html', {'teachers': teachers, 'breadcrumbs': breadcrumbs})


def teacher_detail(request, teacher_slug):
    teacher = get_object_or_404(Teacher, slug=teacher_slug)

    # Migas de pan globales
    breadcrumbs = [
        {'label': 'Profesores', 'url': '/teachers/'},
        {'label': teacher.first_name, 'url': f'/teachers/{teacher_slug}/'},
    ]

    return render(request, 'teacher/teacher_detail.html', {'teacher': teacher, 'breadcrumbs': breadcrumbs})
