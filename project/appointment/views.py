from django.shortcuts import render
from .serializers import AppointmentSerializer
from .models import Appointment
# Create your views here.
from rest_framework import viewsets
class AppointmentViewSets(viewsets.ModelViewSet):
    queryset=Appointment.objects.all()
    serializer_class=AppointmentSerializer

    # custom query set

    def get_queryset(self): # it shows specific patient all appoinment
        queryset=super().get_queryset()
        patient_id=self.request.query_params.get('patient_id')
        if patient_id:
            queryset=queryset.filter(patient_id=patient_id)
        return queryset