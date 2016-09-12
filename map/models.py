from django.db import models

class Category(models.Model):
    label = models.CharField('label', max_length=32, blank=False)
    color = models.PositiveIntegerField('color', blank=False)

class Point(models.Model):
    # consider DecimalField https://docs.python.org/3/library/decimal.html#module-decimal
    latitude = models.FloatField('latitude', blank=False)
    longitude = models.FloatField('longitude', blank=False)
    category = models.ForeignKey(Category)
    label = models.CharField('label', max_length=256)

