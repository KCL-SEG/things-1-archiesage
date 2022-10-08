from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator

class Thing(models.Model):
    name = models.CharField(unique=True, blank=False, max_length=30)
    description = models.CharField(blank=True, max_length=120)
    quantity = models.IntegerField(unique=False, validators = [
        MinValueValidator(0),
        MaxValueValidator(101)
    ])