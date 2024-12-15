from rest_framework import serializers
from .models import AvailableTime,Designation,Doctor,Review,Specialization




# AvailableTime
class AvailableTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model=AvailableTime
        fields='__all__'

# Designation 
class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Designation
        fields='__all__'

# Doctor
class DoctorSerializer(serializers.ModelSerializer):
    designation=serializers.StringRelatedField(many=True)
    specialization=serializers.StringRelatedField(many=True)
    available_time=serializers.StringRelatedField(many=True)
    class Meta:
        model=Doctor
        fields='__all__'

# Review
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields='__all__'

# Specialization
class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Specialization
        fields='__all__'