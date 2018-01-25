from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=50, unique=False)
    email = models.EmailField(max_length=50, blank=True, null=True, verbose_name="Email Address")
    instagram = models.CharField(max_length=50, blank=True, null=True)
    logo = models.CharField(max_length=1000, blank=True, help_text="Link to image to use e.g. instagram logo url")
    country = models.CharField(max_length=100, blank=True)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]