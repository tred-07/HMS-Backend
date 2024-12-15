from django.contrib import admin
from .models import Appointment
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string 
# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display=['doctor_name','patient_name','time']
    def doctor_name(self,obj):
        return obj.doctor
    def patient_name(self,obj):
        return obj.patient
    def time(self,obj):
        return obj.time
    def save_model(self, request, obj, form,change):
        obj.save()
        if obj.APPOINTMENT_STATUS == "Running" and obj.APPOINTMENT_TYPE=="Online":
            email_subject="Confirm your account"
            email_body=render_to_string('confirm_email.html',{'confirm_link':obj.patient.user})
            email=EmailMultiAlternatives(email_subject,"",to=[obj.patient.user.email])
            email.attach_alternative(email_body,"text/html")
            email.send()
    
admin.site.register(Appointment,AppointmentAdmin)