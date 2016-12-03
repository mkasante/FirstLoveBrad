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



# -*- coding: utf-8 -*-

import codecs, cStringIO, csv, json
import sys, requests, os
from collections import OrderedDict


def flatten(l):
	'''
	flattens a list, dict or tuple
	'''
	ret = []
	for i in l:
		if isinstance(i, list) or isinstance(i, tuple):
			ret.extend(flatten(i))
		elif isinstance(i, dict):
			ret.extend(flatten(i.values()))
		else:
			ret.append(i)
	return ret

def convertJsonCsv(appname):
	path = "api/templates/fixtures"
	try:
		if not os.path.exists(path): os.makedirs(path)

		file_json = "https://firstloveleeds.herokuapp.com/api/%s/?format=json" % appname
		data = requests.get(file_json, auth=("firstloveleeds", "14leeds20")).json(object_pairs_hook=OrderedDict)
		file_csv = "%s/%s.csv" % (path, appname)

		data = data['results']
		fields = data[0].keys()

		with open(file_csv, 'wb') as fo:
			writer = csv.DictWriter(fo, fieldnames=fields)
			o = UnicodeWriter(fo)
			o.writerow(fields)

			for record in data:
				o.writerow(flatten(record.values()))
	except:
		pass
		

class UTF8Recoder:
	"""
	Iterator that reads an encoded stream and reencodes the input to UTF-8
	"""
	def __init__(self, f, encoding):
		self.reader = codecs.getreader(encoding)(f)

	def __iter__(self):
		return self

	def next(self):
		return self.reader.next().encode("utf-8")


class UnicodeReader:
	"""
	A CSV reader which will iterate over lines in the CSV file "f",
	which is encoded in the given encoding.
	"""

	def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
		f = UTF8Recoder(f, encoding)
		self.reader = csv.reader(f, dialect=dialect, **kwds)

	def next(self):
		row = self.reader.next()
		return [unicode(s, "utf-8") for s in row]

	def __iter__(self):
		return self


class UnicodeWriter:
	"""
	A CSV writer which will write rows to CSV file "f",
	which is encoded in the given encoding.
	"""

	def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
		# Redirect output to a queue
		self.queue = cStringIO.StringIO()
		self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
		self.stream = f
		self.encoder = codecs.getincrementalencoder(encoding)()

	def writerow(self, row):
		self.writer.writerow([unicode(s).encode("utf-8") for s in row])
		# Fetch UTF-8 output from the queue ...
		data = self.queue.getvalue()
		data = data.decode("utf-8")
		# ... and reencode it into the target encoding
		data = self.encoder.encode(data)
		# write to the target stream
		self.stream.write(data)
		# empty queue
		self.queue.truncate(0)

	def writerows(self, rows):
		for row in rows:
			self.writerow(row)



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