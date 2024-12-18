# Create your models here.
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)  # Category name
    description = models.TextField()  # Category description

    def __str__(self):
        return self.name
