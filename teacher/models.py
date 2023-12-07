# teacher/models.py
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

def upload_avatar_path(filename):
    return f'teachers/{filename}' 

class Teacher(models.Model):
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    slug = models.SlugField(max_length=50)
    subject = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to=upload_avatar_path, blank=True)

    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.first_name + ' ' + self.last_name)
        super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse('teacher:teacher_detail', args=[str(self.slug)])
