from django.conf.urls import url

from member.views import index, member_info, all_members, shepherd_list, shepherd_info
from member.views import _list_members_by_alphabet, _list_members_by_status, _list_members_by_gender, close_proximity_members, close_proximity_followup, signup_firsttimer



urlpatterns = [
  url(
    regex=r'^$',
    view = index, name = 'index'
  ),

  url(
    regex=r'^all/$',
    view = all_members, name = 'all_members'
  ),

  url(
    regex=r'^shepherds/$',
    view = shepherd_list, name = 'shepherd_list'
  ),

  url(
    regex=r'^shepherd/(?P<name>[\w\d\s_\-\.]+)/$',
    view = shepherd_info, name = 'shepherd_info'
  ),

  url(
    regex=r'^signup/firsttimer$',
    view = signup_firsttimer, name = 'signup_firsttimer'
  ),

  url(
    regex=r'^close_proximity_followup/(?P<shepherd>[a-zA-Z]+)/(?P<post_code>[\w\s\d]{6,9})/(?P<mode>[a-zA-Z]+)$',
    view = close_proximity_followup, name = 'close_proximity_followup'
  ),

  url(
    regex=r'^close_proximity_followup/(?P<shepherd>[a-zA-Z]+)/(?P<post_code>[\w\s\d]{6,9})/$',
    view = close_proximity_followup, name = 'close_proximity_followup'
  ),

  url(
    regex=r'^close_proximity_members/(?P<post_code>[\w\s\d]{6,9})/(?P<mode>[a-zA-Z]+)$',
    view = close_proximity_members, name = 'close_proximity_members'
  ),

  url(
    regex=r'^close_proximity_members/(?P<post_code>[\w\s\d]{6,9})/$',
    view = close_proximity_members, name = 'close_proximity_members'
  ),

  url(
    regex=r'^(?P<name>[^\`]+)/$',
    view = member_info, name = 'member_info'
  ),


  # Partial views
  url(
    regex=r'^_group/(?P<alphabet>[a-zA-Z]+)$',
    view = _list_members_by_alphabet, name = '_list_members_by_alphabet'
  ),

  url(
    regex=r'^_status/(?P<status>[\w\s\d\.-_]+)$',
    view = _list_members_by_status, name = '_list_members_by_status'
  ),

  url(
    regex=r'^_gender/(?P<gender>[\w]+)$',
    view = _list_members_by_gender, name = '_list_members_by_gender'
  )
]
