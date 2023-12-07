from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class MusicStyle(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    objects = models.Manager()
    
    def __str__(self) -> str:
        return self.name
def upload_avatar_path(instance, filename):
            return f'competitor/{instance.slug}/{filename}'    
class Competitor(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    slug = models.SlugField(unique=True, blank=True, null=True)
    birthdate = models.DateField(blank=False)
    city = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    hobbies = models.CharField(max_length=255, blank=True)
    avatar = models.ImageField(upload_to=upload_avatar_path, blank=True,)
    music_styles = models.ManyToManyField(MusicStyle, related_name='competitors', blank=True)
    objects = models.Manager()
    
    def __str__(self) -> str:
        return self.first_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.first_name + ' ' + self.last_name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('competitor:competitor_detail', args=[str(self.slug)])
