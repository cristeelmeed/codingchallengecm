from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .schedules import get_available_schedules
from .serializers import AvaliableEmployeeSerializer

class AvaliableEmployeeView(APIView):
    def get(self, request):
        try:
            available_times = get_available_schedules()
            data = [{'time': time_point, 'attendees': attendees} for time_point, attendees in available_times.items()]
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
