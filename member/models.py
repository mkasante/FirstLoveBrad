from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=50, unique=False)
    gender = models.ForeignKey('Gender', on_delete=models.CASCADE, related_name="sex", null=True)
    mobile_no = models.CharField(max_length=50, blank=True, null=True, unique=True, verbose_name="Mobile number")
    email = models.EmailField(max_length=50, blank=True, null=True, verbose_name="Email Address")
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField(max_length=200, blank=True, null=True)
    post_code = models.CharField(max_length=10, blank=True, null=True)
    academic_institution = models.ForeignKey('AcademicInstitution', on_delete=models.CASCADE, 						related_name="academic_institution", null=True, blank=True, )
    course = models.CharField(max_length=100, blank=True)
    first_attended = models.DateField(blank=True, null=True)
    attendance_status = models.ForeignKey('Attendance', on_delete=models.CASCADE, related_name="attendance_status")
    shepherd = models.ForeignKey(User, on_delete=models.CASCADE)
    last_visited = models.DateField(null=True, blank=True)
    extra_info = models.TextField(max_length=2000, blank=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Attendance(models.Model):
    status = models.CharField(max_length=200, unique=True, null=True)

    def __str__(self):
        return self.status

    class Meta:
        ordering = ["status"]
        verbose_name_plural = "Attendance"


class AcademicInstitution(models.Model):
    name = models.CharField(max_length=200, unique=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Gender(models.Model):
    gender = models.CharField(max_length=200, unique=True, null=True)

    def __str__(self):
        return self.gender

    class Meta:
        ordering = ["gender"]
        verbose_name_plural = "Gender"
