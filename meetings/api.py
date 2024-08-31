from meetings.models import Meeting
from rest_framework import viewsets, permissions
from .serializers import MeetingSerializer

class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = MeetingSerializer