from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from rest_framework import viewsets
from api.serializers import MemberSerializer, AttendanceSerializer, AcademicInstitutionSerializer
from api.serializers import EventSerializer, EventTypeSerializer

from member.models import Member, Attendance, AcademicInstitution
from event.models import Event, EventType

from django.http import HttpResponse
from django.core import serializers
import datetime, re, os, requests

from api.json2csv import convertJsonCsv
# Create your views here.
@login_required
def index(request):

	context = {
	}

	return render (request, 'api/index.html', context)


# Serialisers REST Framework
# Member module
class MemberViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = Member.objects.all().order_by('name')
	serializer_class = MemberSerializer


class AttendanceViewSet(viewsets.ModelViewSet):
	queryset = Attendance.objects.all().order_by('status')
	serializer_class = AttendanceSerializer


class AcademicInstitutionViewSet(viewsets.ModelViewSet):
	queryset = AcademicInstitution.objects.all().order_by('name')
	serializer_class = AcademicInstitutionSerializer


# Event module
class EventViewSet(viewsets.ModelViewSet):
	queryset = Event.objects.all().order_by('-date')
	serializer_class = EventSerializer


class EventTypeViewSet(viewsets.ModelViewSet):
	queryset = EventType.objects.all().order_by('name')
	serializer_class = EventType




# API Generator
def write_api(appname):
	url = "https://firstloveleeds.herokuapp.com/api/%s/" % appname
	path = "api/templates/_fixtures"

	try:
		# if not os.dir.exists("api/fixtures"): os.makedirs("api/fixtures")
		if not os.path.exists(path): os.makedirs(path)

		json_data = requests.get(url, auth=("firstloveleeds", "14leeds20")).text
		with open("%s/%s.json" % (path, appname), "w" ) as f:
			f.write(json_data)
	except: pass


def serialize_api(appname, model):
	path = "api/templates/fixtures"
	try:
		if not os.path.exists(path): os.makedirs(path)
		JSONSerializer = serializers.get_serializer("json")
		json_serializer = JSONSerializer()
		
		with open("%s/%s.json" % (path, appname), "w") as out:
			json_serializer.serialize(model.objects.all(), stream=out)
			
	except: pass

# API Generator View
@login_required
def __member_api(request):
	# write_api("member")
	serialize_api("member", Member)

	return render (request, 'fixtures/member.json', content_type="application/json")

@login_required
def __attendance_api(request):
	# write_api("attendance")
	serialize_api("attendance", Attendance)

	return render (request, 'fixtures/attendance.json', content_type="application/json")


@login_required
def __academic_institution_api(request):
	# write_api("academic-institution")
	serialize_api("academic-institution", AcademicInstitution)

	return render (request, 'fixtures/academic-institution.json', content_type="application/json")

@login_required    
def __event_api(request):
	# write_api("event")
	serialize_api("event", Event)

	return render (request, 'fixtures/event.json', content_type="application/json")

@login_required    
def __event_type_api(request):
	# write_api("event")
	serialize_api("event-type", EventType)

	return render (request, 'fixtures/event-type.json', content_type="application/json")



# # To CSV
@login_required
def __member_csv(request):
	convertJsonCsv("member")

	return render (request, 'fixtures/member.csv', content_type="text/csv")


@login_required
def __attendance_csv(request):
	convertJsonCsv("attendance")

	return render (request, 'fixtures/attendance.csv', content_type="text/csv")


@login_required
def __event_csv(request):
	convertJsonCsv("event")

	return render (request, 'fixtures/event.csv', content_type="text/csv")


@login_required
def __academic_institution_csv(request):
	convertJsonCsv("academic-institution")

	return render (request, 'fixtures/academic-institution.csv', content_type="text/csv")