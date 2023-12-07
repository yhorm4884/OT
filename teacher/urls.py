from django.urls import path
from . import views

app_name = 'teacher'
urlpatterns = [
    path('', views.show_teachers, name='teacher_list'),
    path('<slug:teacher_slug>/', views.teacher_detail, name='teacher_detail'),  
]
