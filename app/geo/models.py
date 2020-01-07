from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
# from django.db import models


# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=200)
    lng = models.DecimalField(decimal_places=8, max_digits=12, null=True, blank=True)
    lat = models.DecimalField(decimal_places=8, max_digits=12, null=True, blank=True)
    latlng = models.PointField(null=True, blank=True)

    def __init__(self):
        print('init')
        self.latlng = Point(x=float(self.lat), y=float(self.lng))

        super(Location, self).__init__()

    def __str__(self):
        return self.name

    def __str__(self):
        return f'name[{self.name}] : {self.lat}, {self.lng}, {self.latlng}'

