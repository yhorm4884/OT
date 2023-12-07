from django.urls import path
from . import views

app_name = 'judge'

urlpatterns = [
    path('', views.show_judges, name='judge_list'),
    path('<slug:judge_slug>/', views.judge_detail, name='judge_detail'),
]
