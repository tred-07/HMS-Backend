from django.db import models
from django.contrib.auth.models import User
from patient.models import Patient
# Create your models here.

class Specialization(models.Model):
    name=models.CharField(max_length=40)
    slug=models.SlugField(max_length=40)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural="Specialization"

class Designation(models.Model):
    name=models.CharField(max_length=40)
    slug=models.SlugField(max_length=40)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural="Designation"

class AvailableTime(models.Model):
    name=models.CharField(max_length=40)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural="Available Time"

class Doctor(models.Model):
    # user=models.ForeignKey(User,on_delete=models.CASCADE)
    user=models.CharField(max_length=40,null=True)
    image=models.ImageField(upload_to="doctor/images/",null=True,blank=True)
    designation=models.ManyToManyField(Designation,null=True,blank=True)
    specialization=models.ManyToManyField(Specialization,null=True,blank=True)
    available_time=models.ManyToManyField(AvailableTime,null=True,blank=True)
    fee=models.IntegerField(null=True,blank=True)
    meet_link=models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return f"{self.user}" 
    
    class Meta:
        verbose_name_plural="Doctor"

STAR_CHOICES=[
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐','⭐⭐⭐⭐')
    ]

class Review(models.Model):
    reviewer=models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    choices=models.CharField(max_length=20,choices=STAR_CHOICES)

    class Meta:
        verbose_name_plural='Review'

    def __str__(self):
        return f"{self.reviewer} {self.doctor}"