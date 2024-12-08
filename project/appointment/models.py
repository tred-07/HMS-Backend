from django.db import models
from patient.models import Patient
from doctor.models import Doctor,AvailableTime
# Create your models here.
APPOINTMENT_STATUS=[('Completed','Completed'),('Pending','Pending'),('Running','Running')]
APPOINTMENT_TYPE=[('Offline','Offline'),('Online','Online'),]
class Appointment(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    APPOINTMENT_TYPE=models.CharField(choices=APPOINTMENT_TYPE,max_length=40)
    APPOINTMENT_STATUS=models.CharField(choices=APPOINTMENT_STATUS,max_length=40)
    symtom=models.TextField()
    time=models.OneToOneField(AvailableTime,on_delete=models.CASCADE)
    cancel=models.BooleanField(default=False)
    def __str__(self):
        return f"Doctor: {self.doctor.user},Patient : {self.patient.user.first_name}, Time: {self.time}"
    
    class Meta:
        verbose_name_plural="Appoinment"
