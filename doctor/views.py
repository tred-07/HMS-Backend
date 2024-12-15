from django.shortcuts import render
from rest_framework import viewsets,pagination,filters
from .models import AvailableTime,Designation,Doctor,Review,Specialization
from . import serializers
from rest_framework.permissions import IsAuthenticated

class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        doctor_id=request.query_params.get("doctor_id")
        if doctor_id:
            return queryset.filter(doctor=doctor_id)
        return queryset

class AvailableTimeViewSets(viewsets.ModelViewSet):
    queryset=AvailableTime.objects.all()
    serializer_class=serializers.AvailableTimeSerializer
    filter_backends=[AvailableTimeForSpecificDoctor]

class DesignationViewSets(viewsets.ModelViewSet):
    queryset=Designation.objects.all()
    serializer_class=serializers.DesignationSerializer


class DoctorPagination(pagination.PageNumberPagination):
    page_size=1 # items per page
    page_size_query_param=page_size
    max_page_size=100

class DoctorViewSets(viewsets.ModelViewSet):
    queryset=Doctor.objects.all()
    serializer_class=serializers.DoctorSerializer
    pagination_class=DoctorPagination
    filter_backends=[filters.SearchFilter]

class ReviewViewSets(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset=Review.objects.all()
    serializer_class=serializers.ReviewSerializer

class SpecializationViewSets(viewsets.ModelViewSet):
    queryset=Specialization.objects.all()
    serializer_class=serializers.SpecializationSerializer