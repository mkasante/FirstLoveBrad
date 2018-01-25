import datetime
import os
import re
from firstlove.helpers import file_manager

import requests
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from xlsxwriter.workbook import Workbook

from api.serializers import (AcademicInstitutionSerializer,
                             AttendanceSerializer, EventSerializer,
                             EventTypeSerializer, GenderSerializer,
                             MemberSerializer)
from event.admin import EventAdmin, EventTypeAdmin
from event.models import Event, EventType
from member.admin import (AcademicInstitutionAdmin, AttendanceAdmin,
                          GenderAdmin, MemberAdmin)
from member.models import AcademicInstitution, Attendance, Gender, Member

try:
	import cStringIO as StringIO
except ImportError:
	import StringIO

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

# # To CSV
@login_required
def __member_csv(request):
	members = Member.objects.order_by('name')
	data = file_manager.download_as_csv(request, members, "members")

	return HttpResponse (data, content_type='text/csv')

@login_required
def __gender_csv(request):
	gender = Gender.objects.order_by('gender')
	data = file_manager.download_as_csv(request, gender, "gender")

	return HttpResponse (data, content_type='text/csv')

@login_required
def __attendance_csv(request):
	attendance = Attendance.objects.order_by('status')
	data = file_manager.download_as_csv(request, attendance, "attendance_status")

	return HttpResponse (data, content_type='text/csv')


@login_required
def __event_csv(request):
	events = Event.objects.order_by('-date')
	data = file_manager.download_as_csv(request, events, "event")

	return HttpResponse (data, content_type='text/csv')


@login_required
def __academic_institution_csv(request):
	academic_institutions = AcademicInstitution.objects.order_by('name')
	data = file_manager.download_as_csv(request, academic_institutions, "academic_institutions")

	return HttpResponse (data, content_type='text/csv')


def get_model_data(queryset):
	opts = queryset.model._meta
	model = queryset.model

	field_names = [field.name for field in opts.fields if field.name != "id"]
	field_headers = [x.title().replace("_", " ") for x in field_names ]

	data = []
	for obj in queryset:
		data.append([getattr(obj, field) for field in field_names if field != "id"])

	return field_headers, data




def download_as_excel(request):
    
	# create a workbook in memory
	output = StringIO.StringIO()

	book = Workbook(output)
	sheet = book.add_worksheet('Member')

	format_ = book.add_format({
		'bold': True,
		'font_size': 14
	})
	format2 = book.add_format()

	members = Member.objects.order_by('name')
	header, data = get_model_data(members)

	for x in header:
		sheet.set_column(0, len(header), 30)
		sheet.write(0, header.index(x), x, format_)

	for x in data:
		for y in x:
			sheet.write(data.index(x) + 1, x.index(y), str(y), format2)


	# ========================
	sheet2 = book.add_worksheet('Event')

	events = Event.objects.order_by('-date')
	header, data = get_model_data(events)

	for x in header:
		sheet2.set_column(0, len(header), 30)
		sheet2.write(0, header.index(x), x, format_)

	for x in data:
		for y in x:
			sheet2.write(data.index(x) + 1, x.index(y), str(y), format2)

	# =============================
	sheet3 = book.add_worksheet('Gender')

	gender = Gender.objects.order_by('gender')
	header, data = get_model_data(gender)

	for x in header:
		sheet3.set_column(0, len(header), 30)
		sheet3.write(0, header.index(x), x, format_)

	for x in data:
		for y in x:
			sheet3.write(data.index(x) + 1, x.index(y), str(y), format2)

	# ===================================
	sheet4 = book.add_worksheet('Attendance')

	attendance = Attendance.objects.order_by('status')
	header, data = get_model_data(attendance)

	for x in header:
		sheet4.set_column(0, len(header), 30)
		sheet4.write(0, header.index(x), x, format_)

	for x in data:
		for y in x:
			sheet4.write(data.index(x) + 1, x.index(y), str(y), format2)


	# ===================================
	sheet5 = book.add_worksheet('Event Type')

	event_type = EventType.objects.order_by('name')
	header, data = get_model_data(event_type)

	for x in header:
		sheet5.set_column(0, len(header), 30)
		sheet5.write(0, header.index(x), x, format_)

	for x in data:
		for y in x:
			sheet5.write(data.index(x) + 1, x.index(y), str(y), format2)


	# ===================================
	sheet6 = book.add_worksheet('Academic Institution')

	academic_institutions = AcademicInstitution.objects.order_by('name')
	header, data = get_model_data(academic_institutions)

	for x in header:
		sheet6.set_column(0, len(header), 30)
		sheet6.write(0, header.index(x), x, format_)

	for x in data:
		for y in x:
			sheet6.write(data.index(x) + 1, x.index(y), str(y), format2)

	book.close()


	# construct response
	output.seek(0)
	response = HttpResponse(output.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
	response['Content-Disposition'] = "attachment; filename=firstlove.xlsx"

	return HttpResponse (response, content_type='attachment; filename=firstlove.xlsx')
