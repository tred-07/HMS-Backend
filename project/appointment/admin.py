from django.contrib import admin
from .models import Appointment
# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display=['doctor_name','patient_name','time']
    def doctor_name(self,obj):
        return obj.doctor
    def patient_name(self,obj):
        return obj.patient
    def time(self,obj):
        return obj.time
    
admin.site.register(Appointment,AppointmentAdmin)
