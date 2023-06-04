from django.shortcuts import render
from rest_framework import viewsets

from sales_network.models import Unit
from sales_network.serializers import UnitSerializer


# Create your views here.
class UnitViewSet(viewsets.ModelViewSet):
    serializer_class = UnitSerializer
    queryset = Unit.objects.all()
