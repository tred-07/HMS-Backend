from django.shortcuts import render,redirect,HttpResponse
from rest_framework.routers import DefaultRouter
from rest_framework import viewsets
from .models import Patient
from .serializers import PatientSerializer,RegistrationSerializer,UserLoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import tokens,authenticate,login,logout
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.views import generic
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string 



class UserViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class UserRegistration(APIView): # potato vs round-potato
    serializer_class=RegistrationSerializer

    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            user.is_active=False
            token=tokens.default_token_generator.make_token(user)
            uid=urlsafe_base64_encode(force_bytes(user.pk))
            confirm_link=f"http://127.0.0.1:8000/patient/active/{uid}/{token}"
            email_subject="Confirm your account"
            email_body=render_to_string('confirm_email.html',{'confirm_link':confirm_link})
            email=EmailMultiAlternatives(email_subject,"",to=[user.email])
            email.attach_alternative(email_body,"text/html")
            email.send()
            # user.is_active(False)
            return Response("Done 1")
        return Response(serializer.errors)
    


# def Activate(request,uid,token):
class Activate(generic.View):
    def get(self,request,uid,token):
        try:
            uid=urlsafe_base64_decode(uid).decode()
            user=User. _default_manager.get(pk=uid)
        except(User.DoesNotExist):
            user=None

        if user is not None and tokens.default_token_generator.check_token(user,token):
            user.is_active=True
            user.save()
            return redirect('login')

        return HttpResponse("You are not authenticated user.")


class UserLoginView(APIView):
    def post(self,request):
        serializer=UserLoginSerializer(data=self.request.data)
        if serializer.is_valid():
            username=serializer.validated_data['username']
            password=serializer.validated_data['password']

            user=authenticate(username=username,password=password)
            if user:
                token,_=Token.objects.get_or_create(user=user)
                login(request,user)
                return Response({'token':token.key,'user_id':user.id})
            return HttpResponse("Invalid User")
        return HttpResponse("Invalid User")
    

class UserLogOutView(APIView):
    def get(self,req):
        req.user.auth_token.delete()
        logout(req)
        return redirect('login')