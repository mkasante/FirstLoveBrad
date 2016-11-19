from django.contrib import admin
from member.models import Member
from member.models import MemberAdmin

# Register your models here.
admin.site.register(Member, MemberAdmin)