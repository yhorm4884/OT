from django.contrib import admin
from .models import Teacher

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'subject')
    search_fields = ('first_name', 'last_name', 'slug', 'subject')
admin.site.register(Teacher, TeacherAdmin)