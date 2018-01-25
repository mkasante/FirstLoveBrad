from django.contrib import admin

from member.models import Member
from member.models import Attendance
from member.models import AcademicInstitution
from member.models import Gender

import csv
from django.http import HttpResponse
from firstlove.helpers import admin_actions

class MemberAdmin(admin.ModelAdmin):
    filter_by = ('name', 'mobile_no', 'email')
    list_display = ('name', 'mobile_no', 'email')
    list_filter = ['attendance_status', 'gender', 'shepherd', 'first_attended']
    list_per_page = 50
    order_by = ('name', 'mobile_no')
    search_fields = ('name', 'mobile_no', 'email', 'post_code')
    actions = [admin_actions.export_to_csv]

class AttendanceAdmin(admin.ModelAdmin):
    filter_by = ['status']
    list_filter = ['status']
    list_per_page = 50
    order_by = ['status']
    actions = [admin_actions.export_to_csv]    


class AcademicInstitutionAdmin(admin.ModelAdmin):
    filter_by = ['name']
    list_filter = ['name']
    list_per_page = 50
    order_by = ['name']
    actions = [admin_actions.export_to_csv]    


class GenderAdmin(admin.ModelAdmin):
    filter_by = ['gender']
    list_filter = ['gender']
    list_per_page = 50
    order_by = ['gender']
    actions = [admin_actions.export_to_csv]
    

# Register your models here.
admin.site.register(Member, MemberAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(AcademicInstitution, AcademicInstitutionAdmin)
admin.site.register(Gender, GenderAdmin)