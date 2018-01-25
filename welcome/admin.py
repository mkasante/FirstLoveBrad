from django.contrib import admin
from welcome.models import Organization
from firstlove.helpers import admin_actions

class OrganizationAdmin(admin.ModelAdmin):
    filter_by = ('name', 'email', 'instagram')
    list_display = ('name', 'email', 'instagram')
    list_per_page = 50
    order_by = ('-id', 'name')
    actions = [admin_actions.export_to_csv]
    
# Register your models here.
admin.site.register(Organization, OrganizationAdmin)