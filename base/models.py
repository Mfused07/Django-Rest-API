from django.db import models

# Create your models here.

class Item(models.Model):
    # name string and timestamp of when each instance is created
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

