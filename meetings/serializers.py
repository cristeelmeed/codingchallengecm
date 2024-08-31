from rest_framework import serializers
from .models import Meeting

class AvaliableEmployeeSerializer(serializers.ModelSerializer):
    time = serializers.TimeField()
    employees = serializers.ListField(child=serializers.CharField())
        