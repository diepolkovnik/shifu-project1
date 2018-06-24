from django.db import models

# Create your models here.

class zadanie(models.Model):
    context = models.CharField(max_length=500)
    title = models.CharField(max_length=30)
    slug = models.CharField(max_length=30)
