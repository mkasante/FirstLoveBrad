"""firstlove URL Configuration """
from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.conf import settings
from rest_framework import routers
from api.views import MemberViewSet

import os

admin.autodiscover()
BASE_DIR = os.path.dirname((__file__))

admin.site.site_header = 'First Love Leeds'
admin.site.site_title = 'First Love Leeds'
admin.site.index_css = os.path.join(BASE_DIR, "static/admin", "css/dashboard.css")

router = routers.DefaultRouter()
router.register(r'members', MemberViewSet)

urlpatterns = [
    url(r'^member/', include('member.urls', namespace = "member")),
    url(r'^event/', include('event.urls', namespace = "event")),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', { 'template_name': 'registration/logout.html'}, name='logout'),
    url(r'^welcome/$', include('welcome.urls', namespace = "welcome")),
    url(r'^$', include('welcome.urls', namespace = "welcome")),
	url(r'^api/', include('api.urls', namespace="api")),

	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
]





if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
