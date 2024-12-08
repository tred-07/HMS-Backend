from django.shortcuts import render
from rest_framework.routers import DefaultRouter
from rest_framework import viewsets
from .models import Patient
from .serializers import PatientSerializer
class UserViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer