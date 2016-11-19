from django.db import models
from django.contrib import admin 

# Create your models here.
class Member(models.Model):
	name = models.CharField(max_length=50, unique=True)
	address = models.TextField(max_length=200)
	post_code = models.CharField(max_length=10)
	email = models.EmailField(max_length=50, default="")
	mobile_no = models.CharField(max_length=50, blank=True, unique=True)
	study_place = models.CharField(max_length=50, blank=True)
	course = models.CharField(max_length=100, blank=True)
	date_of_birth = models.DateField(blank=True, null=True)
	first_attended = models.DateField(blank=True)
	last_modified = models.DateTimeField(auto_now=True)
	category = models.CharField(max_length=100, default="")
	extra_info = models.TextField(max_length=2000, blank=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ["name"]

class MemberAdmin(admin.ModelAdmin):
	filter_by = ('name', 'mobile_no', 'email')
	list_display = ('name', 'mobile_no', 'email')
	list_filter = ['category']
	list_per_page = 50
	order_by = ('name', 'mobile_no')
	search_fields = ('name', 'mobile_no', 'email')
