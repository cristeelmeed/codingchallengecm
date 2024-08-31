from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Meeting(models.Model):
    employee = models.ForeignKey(Employee, related_name='meetings', on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.person.name} - {self.start_time} to {self.end_time}"