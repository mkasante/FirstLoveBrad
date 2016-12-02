from member.models import Member, Attendance, AcademicInstitution
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


class MemberSerializer(serializers.HyperlinkedModelSerializer):
	attendance_status = AttendanceSerializer()
	academic_institution = AcademicInstitutionSerializer()

	class Meta:
		model = Member
		fields = ('name', 'address', 'post_code', 'email', 'attendance_status', 'academic_institution',
			'mobile_no', 'course', 'date_of_birth', 'first_attended', 'last_modified', 'extra_info',
			'last_visited',
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


