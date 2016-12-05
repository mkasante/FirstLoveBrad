from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from rest_framework import viewsets
from api.serializers import MemberSerializer, AttendanceSerializer, AcademicInstitutionSerializer
from api.serializers import EventSerializer, EventTypeSerializer, GenderSerializer

from member.models import Member, Attendance, AcademicInstitution, Gender
from member.models import MemberAdmin, AttendanceAdmin, AcademicInstitutionAdmin, GenderAdmin

from event.models import Event, EventType, EventAdmin, EventTypeAdmin 

from django.http import HttpResponse
from django.core import serializers
import datetime, re, os, requests, csv


# =======================================================

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

class GenderViewSet(viewsets.ModelViewSet):
	queryset = Gender.objects.all().order_by('gender')
	serializer_class = Gender



# API Generator View
@login_required
def __member_api(request):
	# write_api("member")
	member = serialize_api("member", Member)
	return HttpResponse(member, content_type="application/json")

@login_required
def __attendance_api(request):
	# write_api("attendance")
	attendance = serialize_api("attendance", Attendance)
	return HttpResponse(attendance, content_type="application/json")




@login_required
def __academic_institution_api(request):
	# write_api("attendance")
	academic_institution = serialize_api("academic-institution", AcademicInstitution)
	return HttpResponse(academic_institution, content_type="application/json")

@login_required    
def __event_api(request):
	# write_api("attendance")
	event = serialize_api("event", Event)
	return HttpResponse(event, content_type="application/json")

@login_required    
def __event_type_api(request):
	# write_api("event")
	event_type = serialize_api("event-type", EventType)
	return HttpResponse(event_type, content_type="application/json")

@login_required    
def __gender_api(request):
	# write_api("gender")
	gender = serialize_api("gender", Gender)

	return HttpResponse(gender, content_type="application/json")



# ===================================
def serialize_api(appname, model):
	models = model.objects.all()
	data = serializers.serialize('json', models)
	return data


def download_csv(modeladmin, request, queryset):
	if not request.user.is_staff:
		raise PermissionDenied

	opts = queryset.model._meta
	model = queryset.model
	response = HttpResponse(content_type='text/csv')

	# force download.
	response['Content-Disposition'] = 'attachment;filename=export.csv'
	# the csv writer
	writer = csv.writer(response)
	field_names = [field.name for field in opts.fields if field.name != "id"]
	field_headers = [x.title().replace("_", " ") for x in field_names ]

	# Write a first row with header information
	writer.writerow(field_headers)


	for obj in queryset:
		writer.writerow([getattr(obj, field) for field in field_names if field != "id"])

	return response



# # To CSV
@login_required
def __member_csv(request):
	members = Member.objects.order_by('name')
	data = download_csv(MemberAdmin, request, members)

	return HttpResponse (data, content_type='text/csv')

@login_required
def __gender_csv(request):
	gender = Gender.objects.order_by('gender')
	data = download_csv(GenderAdmin, request, gender)

	return HttpResponse (data, content_type='text/csv')

@login_required
def __attendance_csv(request):
	attendance = Attendance.objects.order_by('status')
	data = download_csv(AttendanceAdmin, request, attendance)

	return HttpResponse (data, content_type='text/csv')


@login_required
def __event_csv(request):
	events = Event.objects.order_by('-date')
	data = download_csv(EventAdmin, request, events)

	return HttpResponse (data, content_type='text/csv')


@login_required
def __academic_institution_csv(request):
	academic_institutions = AcademicInstitution.objects.order_by('name')
	data = download_csv(AcademicInstitutionAdmin, request, academic_institutions)

	return HttpResponse (data, content_type='text/csv')


