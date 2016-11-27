# from django.contrib.auth.models import User, Group
# from rest_framework import serializers


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'groups')


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name')


from member.models import Member
from rest_framework import serializers

class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = (
        	"name",
			# "address",
			# "post_code",
			# "email",
			# "mobile_no",
			# "course",
			# "date_of_birth",
			# "first_attended",
			# "last_modified",
			# "extra_info",
			# "academic_institution",
			# "attendance_status"
        )