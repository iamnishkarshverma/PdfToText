from django.db import models

# Create your models here.
# models.py

class CV(models.Model):
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    text = models.TextField()
