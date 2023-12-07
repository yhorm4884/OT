from django.db import models
from django.urls import reverse
from django.utils.text import slugify

def upload_avatar_path(filename):
        return f'judge/{filename}' 
class Judge(models.Model):
    first_name = models.CharField(max_length=255,blank=False)
    last_name = models.CharField(max_length=255,blank=False)
    slug = models.SlugField(max_length=50)
    job = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to=upload_avatar_path, blank=True,)
    
    def __str__(self) -> str:
        return self.first_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.first_name + ' ' + self.last_name)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('judge:judge_detail', args=[str(self.slug)])
