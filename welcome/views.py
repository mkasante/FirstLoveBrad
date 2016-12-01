from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core import serializers

from member.models import Member, Attendance, AcademicInstitution
from event.models import Event, EventType

import datetime, re, os, requests



# Create your views here.
@login_required
def index(request):

	context = {
	}

	return render (request, 'newsfeed.html', context)


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
	first_timers = Member.objects.filter(attendance_status__status = "First Timer")[:10]

	context = {
		'first_timers': first_timers
	}

	return render (request, '_partial/_firsttimers.html', context)


@login_required
def _get_evangelismlist(request):
	now = datetime.datetime.now()
	evangelism = Member.objects.filter(attendance_status__status = "Evangelism").order_by('-first_attended')[:10]

	context = {
		'evangelism': evangelism
	}

	return render (request, '_partial/_evangelism.html', context)


# API Generator
def write_api(appname):
	url = "https://firstloveleeds.herokuapp.com/api/%s/" % appname
	try:
		# if not os.dir.exists("api/fixtures"): os.makedirs("api/fixtures")
		if not os.path.exists("_data/_fixtures"): os.makedirs("_data/_fixtures")

		json_data = requests.get(url, auth=("firstloveleeds", "14leeds20")).text
		with open("_data/_fixtures/%s.json" % appname, "w" ) as f:
			f.write(json_data)
	except: pass


def serialize_api(appname, model):
	path = "api/fixtures"
	try:
		if not os.path.exists(path): os.makedirs(path)
		JSONSerializer = serializers.get_serializer("json")
		json_serializer = JSONSerializer()
		with open("%s/%s.json" % (path, appname), "w") as out:
			json_serializer.serialize(model.objects.all(), stream=out)

	except: pass

# API Generator View

def __member_api(request):
	# write_api("member")
	serialize_api("member", Member)

	return HttpResponse("")

def __attendance_api(request):
	# write_api("attendance")
	serialize_api("attendance", Attendance)

	return HttpResponse("")

def __academin_institution_api(request):
	# write_api("academic-institution")
	serialize_api("academic-institution", AcademicInstitution)

	return HttpResponse("")
	
def __event_api(request):
	# write_api("event")
	serialize_api("event", Event)
	serialize_api("event-type", EventType)

	return HttpResponse("")

	