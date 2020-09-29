from django.db import models

# Create your models here.

class basedata(models.Model):
    R = models.CharField(max_length=20)
    G = models.CharField(max_length=20)
    B = models.CharField(max_length=20)
    EX = models.CharField(max_length=20)
    LI = models.CharField(max_length=20)
    BF3 = models.CharField(max_length=20)
    RF3 = models.CharField(max_length=20)
    GF2 = models.CharField(max_length=20)