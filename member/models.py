from django.db import models
from django.contrib import admin 

# Create your models here.
class Member(models.Model):
	name = models.CharField(max_length=50, unique=True)
	address = models.TextField(max_length=200, blank=True, null=True)
	post_code = models.CharField(max_length=10, blank=True, null=True)
	email = models.EmailField(max_length=50, default="", blank=True, null=True)
	mobile_no = models.CharField(max_length=50, blank=True, unique=True)
	course = models.CharField(max_length=100, blank=True)
	date_of_birth = models.DateField(blank=True, null=True)
	first_attended = models.DateField(blank=True, null=True)
	last_modified = models.DateTimeField(auto_now=True)
	extra_info = models.TextField(max_length=2000, blank=True)
	last_visited = models.DateField(null=True, blank=True)
	academic_institution = models.ForeignKey('AcademicInstitution', on_delete=models.CASCADE, related_name="academic_institution", null=True, blank=True)
	attendance_status = models.ForeignKey('Attendance', on_delete=models.CASCADE, related_name="attendance_status")

	def __str__(self):
		return self.name

	class Meta:
		ordering = ["name"]

class MemberAdmin(admin.ModelAdmin):
	filter_by = ('name', 'mobile_no', 'email')
	list_display = ('name', 'mobile_no', 'email')
	list_filter = ['attendance_status']
	list_per_page = 50
	order_by = ('name', 'mobile_no')
	search_fields = ('name', 'mobile_no', 'email')


class Attendance(models.Model):
	status = models.CharField(max_length=200, unique=True, null=True)

	def __str__(self):
		return self.status

	class Meta:
		ordering = ["status"]

class AttendanceAdmin(admin.ModelAdmin):
	filter_by = ['status']
	list_filter = ['status']
	list_per_page = 50
	order_by = ['status']


class AcademicInstitution(models.Model):
	name = models.CharField(max_length=200, unique=True, null=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ["name"]

class AcademicInstitutionAdmin(admin.ModelAdmin):
	filter_by = ['name']
	list_filter = ['name']
	list_per_page = 50
	order_by = ['name']	