from django.conf.urls import url

from event.views import index
# from member.views import _sort_members_by_alphabet, _sort_members_by_status



urlpatterns = [
  url(
    regex=r'^$',
    view = index, name = 'index'
  )
]