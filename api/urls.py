from django.conf.urls import url
from api.views import index
from api.views import MemberViewSet, AttendanceViewSet, AcademicInstitutionViewSet
from api.views import EventViewSet, EventTypeViewSet


urlpatterns = [
  url(
    regex=r'^$',
    view = index, name = 'index'
  ),

  # Member module
  url(
    regex=r'^[mM]ember/$',
    view = MemberViewSet.as_view({'get': 'list'}), name = 'member-detail'
  ),

  url(
    regex=r'^[Aa]ttendance/$',
    view = AttendanceViewSet.as_view({'get': 'list'}), name = 'attendance-detail'
  ),

  url(
    regex=r'^[Aa]cademic-[Ii]nstitution/$',
    view = AcademicInstitutionViewSet.as_view({'get': 'list'}), name = 'academic-institution-detail'
  ),

  # Event module

  url(
    regex=r'^[Ee]vent/$',
    view = EventViewSet.as_view({'get': 'list'}), name = 'event-detail'
  ),



  # url(
  #   regex=r'^[Ee]vent-type/$',
  #   view = EventTypeViewSet.as_view({'get': 'list'}), name = 'event-type-detail'
  # ),

]