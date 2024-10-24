from django.db import models

# Create your models here.
class Logged(models.Model):
    name = models.CharField(max_length=122)
    password = models.CharField(max_length=122)