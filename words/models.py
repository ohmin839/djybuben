from django.db import models

# Create your models here.

class SampledWord(models.Model):
    text = models.TextField(unique=True)
