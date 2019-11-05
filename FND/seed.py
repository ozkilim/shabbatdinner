import os
from faker import Faker
from compressor.offline import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'therapy.settings')

django.setup()

from main.models import *

fake = Faker()

# generate the fake info here

def create_patient_users(number):
	'''create x users'''
	users = []
	for i in range(0, number):
		password = gen_password()
		fname = gen_fname()
		lname = gen_lname()
		username = fname.lower() + lname.lower()
		user = User.objects.create_user(username=username, password=password, first_name=fname, last_name=lname, is_patient=True)
		user.save()
		userdict = {'username' : username, 'password' : password}
		users.append(userdict)
	print(users)