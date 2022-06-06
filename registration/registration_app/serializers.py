from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Applicant, Program, DiscountCode


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email']


class ApplicantSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Applicant
        fields = '__all__'


class ProgramSerializer(serializers.ModelSerializer):

    class Meta:
        model = Program
        fields = '__all__'


class DiscountCodeSerializer(serializers.ModelSerializer):
    applied_by = ApplicantSerializer(many=True)
    
    class Meta:
        model = DiscountCode
        fields = '__all__'