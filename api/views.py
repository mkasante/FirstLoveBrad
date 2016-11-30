from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from rest_framework import viewsets
from api.serializers import MemberSerializer, AttendanceSerializer, AcademicInstitutionSerializer
from api.serializers import EventSerializer, EventTypeSerializer

from member.models import Member, Attendance, AcademicInstitution
from event.models import Event, EventType


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