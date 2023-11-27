from django.db import models


class MusicStyle(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    
class Competitor (models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    slug = models.SlugField(max_length=255)
    birthdate = models.DateTimeField(blank=False)
    subject = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    hobbies = models.CharField(max_length=255, blank=True)
    avatar = models.ImageField(upload_to='competitor/%s' % (slug))
    music_styles = models.ManyToManyField(MusicStyle, related_name='competitors', blank=True)