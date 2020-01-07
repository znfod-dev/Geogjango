from django.contrib.gis.geos import Point
from django.http import HttpResponse
from django.shortcuts import render


from geo.models import Location


def position_list(request):
    pnt = Point(float(37.297055), float(126.862544))

    return HttpResponse('hello world')

