from django.shortcuts import render
from rest_framework import viewsets
from app.models import Employee
from app.serializer import Employeeserializer

class Employeeviewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = Employeeserializer
