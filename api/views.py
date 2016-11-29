from rest_framework import viewsets
from api.serializers import MemberSerializer
from member.models import Member
# Serialisers REST Framework
class MemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Member.objects.all().order_by('name')
    serializer_class = MemberSerializer