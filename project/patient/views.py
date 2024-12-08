from django.shortcuts import render
from rest_framework.routers import DefaultRouter
from rest_framework import viewsets
from .models import Patient
from .serializers import PatientSerializer,RegistrationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
class UserViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class UserRegistration(APIView): # potato vs round-potato
    serializer_class=RegistrationSerializer

    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            print(user)
            return Response("Done 1")
        return Response(serializer.errors)
