from django.contrib import admin

from member.models import Member
from member.models import Attendance
from member.models import AcademicInstitution
from member.models import Gender

from member.models import MemberAdmin
from member.models import AttendanceAdmin
from member.models import AcademicInstitutionAdmin
from member.models import GenderAdmin


# Register your models here.
admin.site.register(Member, MemberAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(AcademicInstitution, AcademicInstitutionAdmin)
admin.site.register(Gender, GenderAdmin)