from django.contrib import admin

from welcome.models import Organization, OrganizationAdmin


# Register your models here.
admin.site.register(Organization, OrganizationAdmin)