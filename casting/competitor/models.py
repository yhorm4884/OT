from django.db import models
from django.urls import reverse

class MusicStyle(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    objects = models.Manager()
    
    def __str__(self) -> str:
        return self.name
    
class Competitor(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    slug = models.SlugField(max_length=255)
    birthdate = models.DateField(blank=False)
    city = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    hobbies = models.CharField(max_length=255, blank=True)
    avatar = models.ImageField(upload_to='competitor/%s' % (slug), blank=True, null=False)
    music_styles = models.ManyToManyField(MusicStyle, related_name='competitors', blank=True)
    objects = models.Manager()

    def __str__(self) -> str:
        return self.first_name

    def get_absolute_url(self):
        return reverse("competitor/competitor_detail.html", args=[self.id])
