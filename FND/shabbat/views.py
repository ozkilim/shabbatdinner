from django.shortcuts import render

from django.core.mail import send_mail
from .models import GroupA, GroupB , GroupOfEight
import dateutil

import datetime
import datetime as DT

import dateutil.relativedelta as REL

today = DT.date.today()
rd = REL.relativedelta(days=1, weekday=REL.FR)
next_friday = today + rd



# Create your views here.
def index(request):
	if request.method=="POST":
		organiser_name=request.POST['organiser_name']
		organiser_email=request.POST['organiser_email']
		name2=request.POST['name2']
		name3=request.POST['name3']
		name4=request.POST['name4']
		group_name=request.POST['group_name']

		'''small peice of code to get out the next friday in a variable..
		'''
		# send_mail('You have been matched!','You have been matched for dinenr on {}'.format(next_friday) ,
		# 'ozkilimportraits@gmail.com',[organiser_email], fail_silently=False)
		context = {'name':organiser_name , 'date':next_friday}
		group_a = GroupA(name2=name2,name3=name3,name4=name4, organiser_email=organiser_email)
		group_a.save()

		trial = GroupA.objects.filter(status='unmatched')[0]
		trial.status='matched'
		trial.save()

		'''this gets the first unmatched value--- the thing is that you get put into a waiting line.... how to deal with this'''
		
		group_b_unmatched = GroupB.objects.filter(status='unmatched')[0]
		group_b_unmatched.status='matched'
		group_b_unmatched.save()

		# GroupOfEight(organiser_name_a= organiser_name, organiser_name_b=, organiser_email_a=organiser_email, organiser_email_b=)
		return render(request,"thankyou.html" , context)
	else:
		return render(request, "front.html")


def index_hebrew(request):
	if request.method=="POST":
		organiser_name=request.POST['organiser_name']
		organiser_email=request.POST['organiser_email']
		name2=request.POST['name2']
		name3=request.POST['name3']
		name4=request.POST['name4']
		group_name=request.POST['group_name']

		'''small peice of code to get out the next friday in a variable..
		'''
		import datetime as DT
		import dateutil.relativedelta as REL
		today = DT.date.today()
		rd = REL.relativedelta(days=1, weekday=REL.FR)
		next_friday = today + rd
		
		# send_mail('You have been matched!','You have been matched for dinenr on {}'.format(next_friday) ,
		# 'ozkilimportraits@gmail.com',[organiser_email], fail_silently=False)
		context = {'name':organiser_name , 'date':next_friday}

		group_b = GroupB(name2=name2,name3=name3,name4=name4, organiser_email=organiser_email)
		group_b.save()


		trial = GroupA.objects.filter(status='unmatched')[0]
		trial.status='matched'
		trial.save()

		'''this gets the first unmatched value--- the thing is that you get put into a waiting line.... how to deal with this'''
		
		group_b_unmatched = GroupB.objects.filter(status='unmatched')[0]
		group_b_unmatched.status='matched'
		group_b_unmatched.save()

		return render(request,"thankyou.html" , context)
	else:
		return render(request, "front.html")


def matcher():

	"""this fucntion matches a group b for the group a 
	that had signedin and renders a page that gives their details and 
	sends an email automatically with the details of group b 
	then blocks you out of the front page ?
	find how to send automatic email with the 
	data from gmail account to email inputted?..
	"""
# 	group_a=GroupA()
# 	are_they_matched = GroupA.objects.all()
# 	print(are_they_matched)

# matcher()

# https://codemyui.com/button-to-email-subscription-field/
# use this! its very cool ui

def hello(request):
	return render(request, "trialfrontend.html")



