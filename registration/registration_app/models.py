from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

from datetime import datetime

class Applicant(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
	civil_id_number = models.CharField(max_length=100, blank=True, null=True)
	date_of_birth = models.DateField(blank=True, null=True)

	def __str__(self):
		return str(self.user)


# @receiver(post_save, sender=User)
# def create_profile(sender, **kwargs):
# 	if kwargs.get('created', False):
# 		Applicant.objects.get_or_create(user= kwargs.get('instance'),)


class Program(models.Model):
	AGES = (
		('10-15', '10-15'),
		('16-20', '16-20'),
		('21-25', '21-25'),
		('26-30', '26-30'),
	)
	name = models.CharField(max_length=100, blank=True, null=True)
	image = models.ImageField(blank=True, null=True)
	date = models.DateTimeField(blank=True, null=True)
	fees = models.CharField(max_length=100, blank=True, null=True)
	age_group = models.CharField(max_length=100, blank=True, null=True, choices=AGES)
	description = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.name


class Staff(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return str(self.user)


class DiscountCode(models.Model):
	code = models.CharField(max_length=100, blank=True, null=True)
	percentage = models.PositiveIntegerField(blank=True, null=True)
	created_at = models.DateTimeField(blank=True, null=True)
	creator = models.OneToOneField(Staff, on_delete=models.CASCADE, blank=True, null=True)
	applied_by = models.ManyToManyField(Applicant, related_name="applicants", blank=True)

	def __str__(self):
		return str(self.code)
