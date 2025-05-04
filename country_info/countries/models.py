from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)
    cca2 = models.CharField(max_length=3)
    capital = models.CharField(max_length=100, blank=True, null=True)
    population = models.IntegerField()
    region = models.CharField(max_length=100)
    timezones = models.JSONField()
    languages = models.JSONField()
    flag = models.URLField()
    
    def __str__(self):
        return self.name