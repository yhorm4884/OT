from django.shortcuts import redirect,render

def dashboard(request):
    competitor_image = 'media/concursantes.jpg'
    judges_image = 'media/jurado.jpg'
    teachers_image = 'media/profesores.jpg'
    return render(request, 'dashboard.html', {'competitor_image': competitor_image, 'judges_image': judges_image, 'teachers_image': teachers_image})
