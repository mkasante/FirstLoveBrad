from django.db import models
from django.contrib import admin

# Create your models here.
class Event(models.Model):
	name = models.ForeignKey('EventType', on_delete=models.CASCADE, related_name="event_type")
	date = models.DateTimeField()
	attendance_count = models.IntegerField()
	venue = models.CharField(max_length=100)
	room = models.CharField(max_length=100, default="")

	def __str__(self):
		return self.name.name

	class Meta:
		ordering = ["-date"]

class EventAdmin(admin.ModelAdmin):
	filter_by = ['name']
	list_display = ['name', 'attendance_count', 'date']
	list_filter = ['name']
	list_per_page = 50
	order_by = ('name', 'attendance_count')
	search_fields = ('name', 'venue')


class EventType(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ["name"]

class EventTypeAdmin(admin.ModelAdmin):
	filter_by = ['name']
	list_filter = ['name']
	list_per_page = 50
	order_by = ['name']
	search_fields = ['name']