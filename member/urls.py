from django.conf.urls import url
from member.views import index

urlpatterns = [
  url(
    regex=r'^$',
    view = index,
    name = 'index'
  ),
]