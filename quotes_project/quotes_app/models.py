from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=100)
    born_date = models.CharField(max_length=100, blank=True, null=True)
    born_location = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Quote(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='quotes')
    text = models.TextField()
    tags = models.CharField(max_length=200)  # Seperate '.' ???

    def __str__(self):
        return f"{self.text[:50]}..."  # Show first 50 characters
