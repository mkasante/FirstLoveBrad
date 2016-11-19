from django.contrib import admin

from member.models import Member
from member.models import Attendance
from member.models import AcademicInstitution

from member.models import MemberAdmin
from member.models import AttendanceAdmin
from member.models import AcademicInstitutionAdmin


# Register your models here.
admin.site.register(Member, MemberAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(AcademicInstitution, AcademicInstitutionAdmin)