from django.conf.urls import url
from api.views import index
from api.views import MemberViewSet, AttendanceViewSet, AcademicInstitutionViewSet, GenderViewSet
from api.views import EventViewSet, EventTypeViewSet

from api.views import __attendance_api, __member_api, __academic_institution_api, __event_api, __event_type_api, __gender_api
from api.views import __attendance_csv, __member_csv, __academic_institution_csv, __event_csv, __gender_csv, __download_excel


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

  url(
    regex=r'^[Gg]ender/$',
    view = GenderViewSet.as_view({'get': 'list'}), name = 'gender-detail'
  ),
  # Event module

  url(
    regex=r'^[Ee]vent/$',
    view = EventViewSet.as_view({'get': 'list'}), name = 'event-detail'
  ),

  url(
    regex=r'^[Ee]vent-type/$',
    view = EventTypeViewSet.as_view({'get': 'list'}), name = 'eventtype-detail'
  ),

# API
  url(
    regex=r'^model/member.json$',
    view = __member_api,
    name = '__member_api'
  ),

  url(
    regex=r'^model/attendance.json$',
    view = __attendance_api,
    name = '__attendance_api'
  ),

  url(
    regex=r'^model/event.json$',
    view = __event_api,
    name = '__event_api'
  ),

  url(
    regex=r'^model/event-type.json$',
    view = __event_type_api,
    name = '__event_type_api'
  ),

  url(
    regex=r'^model/academic-institution.json$',
    view = __academic_institution_api,
    name = '__academic_institution_api'
  ),

  url(
    regex=r'^model/gender.json$',
    view = __gender_api,
    name = '__gender_api'
  ),

# CSV API
  url(
    regex=r'^model/member.csv$',
    view = __member_csv,
    name = '__member_csv'
  ),

  url(
    regex=r'^model/attendance.csv$',
    view = __attendance_csv,
    name = '__attendance_csv'
  ),

  url(
    regex=r'^model/event.csv$',
    view = __event_csv,
    name = '__event_csv'
  ),

  # url(
  #   regex=r'^model/event-type.csv$',
  #   view = __event_type_csv,
  #   name = '__event_type_csv'
  # ),

  url(
    regex=r'^model/academic-institution.csv$',
    view = __academic_institution_csv,
    name = '__academic_institution_csv'
  ),

  url(
    regex=r'^model/gender.csv$',
    view = __gender_csv,
    name = '__gender_csv'
  ),

  url(
    regex=r'^model/firstlove.xlsx$',
    view = __download_excel,
    name = '__download_excel'
  ),
]