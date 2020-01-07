from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
# from django.db import models


# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=200)
    # brew install gdal --HEAD
    # sudo easy_install GDAL

    def __str__(self):
        return self.name


