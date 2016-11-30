from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from member.views import Member
import datetime

# Create your views here.
@login_required
def index(request):

	context = {
	}

	return render (request, 'newsfeed.html', context)

# @login_required
# def newsfeed(request):
# 	context = {}

# 	return render (request, 'newsfeed.html', context)





# 
@login_required
def _get_birthdays(request):
	now = datetime.datetime.now()
	members = Member.objects.all()

	member_dob = []
	for x in members:
		if x.date_of_birth != None:
			dob_month = x.date_of_birth.month
			dob_day = x.date_of_birth.day
			dob_year = x.date_of_birth.year

			if ((int(dob_month) == now.month)
				and int(dob_day) > now.day):
				remaining_day = now.day - int(dob_day)
				age = now.year - int(dob_year)

				member_dob.append((x, age, remaining_day))


	context = {
		'member_dob': member_dob
	}

	return render (request, '_partial/_birthdays.html', context)

@login_required
def _get_firsttimers(request):
	now = datetime.datetime.now()
	members = Member.objects.filter(attendance_status__status = "First Timer")
	first_timers = members

	context = {
		'first_timers': first_timers
	}

	return render (request, '_partial/_firsttimers.html', context)