from rest_framework import serializers
from .models import Patient
from django.contrib.auth.models import User
class PatientSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(many=False)
    class Meta:
        model=Patient
        fields='__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password=serializers.CharField(required=True)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password','confirm_password']

    def save(self):
        username=self.validated_data['username']
        first_name=self.validated_data['first_name']
        last_name=self.validated_data['last_name']
        email=self.validated_data['email']
        password=self.validated_data['password']
        confirm_password=self.validated_data['confirm_password']

        if password!=confirm_password:
            raise serializers.ValidationError({'error':'Password Does Not Match'})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error':'Email already exist'})
        account=User(username=username,first_name=first_name,last_name=last_name,email=email)
        account.set_password(password)
        account.save()
        print(account)
        return account