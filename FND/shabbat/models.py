from django.db import models
from django.contrib.auth.models import User

class GroupA(models.Model):
	organiser_name=models.CharField(max_length=100)
	name2=models.CharField(max_length=100)
	name3=models.CharField(max_length=100)
	name4=models.CharField(max_length=100)
	organiser_email=models.CharField(max_length=100)
	status = models.CharField(max_length=7, default='unmatched', editable=True)


class GroupB(models.Model):
	organiser_name=models.CharField(max_length=100)
	name2=models.CharField(max_length=100)
	name3=models.CharField(max_length=100)
	name4=models.CharField(max_length=100)
	organiser_email=models.CharField(max_length=100)
	status = models.CharField(max_length=7, default='unmatched', editable=True)



class User(models.Model):
	user_name=models.CharField(max_length=100)


class GroupOfEight(models.Model):
	organiser_name_a=models.CharField(max_length=100)
	organiser_name_b=models.CharField(max_length=100)
	organiser_email_a=models.CharField(max_length=100)
	organiser_email_b=models.CharField(max_length=100)

