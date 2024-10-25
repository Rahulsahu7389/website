from django.db import models

# Create your models here.
class Logged(models.Model):
    name = models.CharField(max_length=122)
    password = models.CharField(max_length=122)

class Templ(models.Model):
    name1 = models.CharField(max_length=122)
    name2 = models.CharField(max_length=122)
    name3 = models.CharField(max_length=122)
    name4 = models.CharField(max_length=122)
    # name5 = models.CharField(max_length=122)

class Template1(models.Model):
    name1 = models.CharField(max_length=122)
    name2 = models.CharField(max_length=122)
    name3 = models.CharField(max_length=122)
    name4 = models.CharField(max_length=122)
    name5 = models.CharField(max_length=122)

