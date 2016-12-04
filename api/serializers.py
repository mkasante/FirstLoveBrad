from member.models import Member, Attendance, AcademicInstitution, Gender
from event.models import Event, EventType
from rest_framework import serializers

# Member models
class AttendanceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Attendance
		# fields = "__all__"
		exclude = ('id',)

class AcademicInstitutionSerializer(serializers.ModelSerializer):
	class Meta:
		model = AcademicInstitution
		exclude = ('id',)

class GenderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Gender
		exclude = ('id',)

class MemberSerializer(serializers.HyperlinkedModelSerializer):
	attendance_status = AttendanceSerializer()
	academic_institution = AcademicInstitutionSerializer()
	gender = GenderSerializer()
	class Meta:
		model = Member
		fields = ('name', 'gender', 'date_of_birth', 'email', 'mobile_no', 'address', 'post_code', 'attendance_status', 'academic_institution', 'course', 'first_attended', 'extra_info', 'last_visited', 'last_modified'
		)



# Event models
class EventTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = EventType
		exclude = ('id',)

class EventSerializer(serializers.HyperlinkedModelSerializer):
	event = EventTypeSerializer()
	class Meta:
		model = Event
		fields = ("date", "event", "venue", "room", "attendance_count", "first_timers_count", "born_again_count",
			 "last_modified"
		)


