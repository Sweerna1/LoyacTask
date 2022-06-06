from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView
from rest_framework.response import Response

from .models import Applicant, Program, DiscountCode
from .serializers import ApplicantSerializer, ProgramSerializer, DiscountCodeSerializer


class UserLogin(APIView):
	
	def post(self, request):
		username = request.data['username']
		password = request.data['password']

		auth_user = authenticate(username=username, password=password)

		if auth_user is not None:
			applicant = Applicant.objects.get(user=auth_user)
			serializer_class = ApplicantSerializer(applicant)
			login(request, auth_user)
			return Response(status=status.HTTP_200_OK, data=serializer_class.data)
		return Response(status=status.HTTP_400_BAD_REQUEST)


class ProgramsList(APIView):
	
	def get(self, request):
		programs = Program.objects.all()
		serializer_class = ProgramSerializer(programs, many=True)
		return Response(status=status.HTTP_200_OK, data=serializer_class.data)


class DiscountCodesList(APIView):
	
	def get(self, request):
		discount_codes = DiscountCode.objects.all()
		serializer_class = DiscountCodeSerializer(discount_codes, many=True)
		return Response(status=status.HTTP_200_OK, data=serializer_class.data)


class SubmitOrder(APIView):

	def post(self,request):
		print("request.data", request.data)
		return Response(status=status.HTTP_200_OK)		
