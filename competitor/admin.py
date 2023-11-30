from django.contrib import admin
from .models import Competitor, MusicStyle

class MusicStyleAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

admin.site.register(MusicStyle, MusicStyleAdmin)

class CompetitorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birthdate', 'city', 'job', 'hobbies')
    search_fields = ('first_name', 'last_name', 'city', 'job')
    filter_horizontal = ('music_styles',)
admin.site.register(Competitor, CompetitorAdmin)