from django.conf.urls import url

from member.views import index, member_info, all_members  
from member.views import _list_members_by_alphabet, _list_members_by_status



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
    regex=r'^(?P<name>[^\`]+)/$',
    view = member_info, name = 'member_info'
  ),


  # Partial views
  url(
    regex=r'^_group/(?P<alphabet>[a-zA-Z]+)$',
    view = _list_members_by_alphabet, name = '_list_members_by_alphabet'
  ),

  url(
    regex=r'^_status/(?P<status_id>[\w\s\d]+)$',
    view = _list_members_by_status, name = '_list_members_by_status'
  )

]