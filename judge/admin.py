from django.contrib import admin
from .models import Judge

class JudgeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'job')
    search_fields = ('first_name', 'last_name', 'slug', 'job')
admin.site.register(Judge, JudgeAdmin)