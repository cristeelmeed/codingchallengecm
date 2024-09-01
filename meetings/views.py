from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import find_available_schedules
from .serializers import AvaliableEmployeeSerializer

class AvaliableEmployeeView(APIView):
    def get(self, request):
        try:
            available_times = find_available_schedules()
            data = [{'time': time_point, 'employees': employees} for time_point, employees in available_times.items()]
            serializer = AvaliableEmployeeSerializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
