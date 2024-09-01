from rest_framework import serializers

class AvaliableEmployeeSerializer(serializers.Serializer):
        time = serializers.TimeField()
        employees = serializers.ListField(child=serializers.CharField())
        