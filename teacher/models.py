from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=255,blank=False)
    last_name = models.CharField(max_length=255,blank=False)
    slug = models.SlugField(max_length=50)
    subject = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='teacher/%s' % (slug))