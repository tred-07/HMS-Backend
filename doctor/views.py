from django.shortcuts import render
from rest_framework import viewsets
from .models import AvailableTime,Designation,Doctor,Review,Specialization
from . import serializers
class AvailableTimeViewSets(viewsets.ModelViewSet):
    queryset=AvailableTime.objects.all()
    serializer_class=serializers.AvailableTimeSerializer

class DesignationViewSets(viewsets.ModelViewSet):
    queryset=Designation.objects.all()
    serializer_class=serializers.DesignationSerializer

class DoctorViewSets(viewsets.ModelViewSet):
    queryset=Doctor.objects.all()
    serializer_class=serializers.DoctorSerializer

class ReviewViewSets(viewsets.ModelViewSet):
    queryset=Review.objects.all()
    serializer_class=serializers.ReviewSerializer

class SpecializationViewSets(viewsets.ModelViewSet):
    queryset=Specialization.objects.all()
    serializer_class=serializers.SpecializationSerializer