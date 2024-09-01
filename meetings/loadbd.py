import sys
from pathlib import Path
sys.path.append(Path(__file__).resolve().parent.parent.__str__())
print (sys.path)

import os
import django
from datetime import time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codingchallengecm.settings')
django.setup()

from meetings.models import Employee, Meeting

def load_data():
    employees = [
        'Kyle', 'Paul', 'Alex', 'Luis', 'Jairo', 'Sonya'
    ]

    for name in employees:
        Employee.objects.get_or_create(name=name)

    meetings = {
        'Kyle': [('13:30', '14:00'), ('14:30', '15:00'), ('18:00', '18:30')],
        'Paul': [('07:00', '07:30'), ('09:00', '09:30'), ('13:30', '14:00'), ('15:00', '15:30'), ('15:30', '16:00')],
        'Alex': [('08:00', '08:30'), ('09:30', '10:00'), ('12:30', '13:00'), ('15:00', '15:30')],
        'Luis': [('09:00', '09:30'), ('13:30', '14:00'), ('15:00', '15:30'), ('15:30', '16:00')],
        'Jairo': [('08:00', '08:30'), ('09:00', '09:30'), ('18:00', '18:30')],
        'Sonya': [('08:00', '08:30'), ('12:30', '13:00'), ('13:30', '14:00'), ('15:30', '16:00')]
    }

    for employee_name, times in meetings.items():
        employee = Employee.objects.get(name=employee_name)
        for start, end in times:
            start_time = time.fromisoformat(start)
            end_time = time.fromisoformat(end)
            Meeting.objects.get_or_create(employee=employee, start_time=start_time, end_time=end_time)

if __name__ == '__main__':
    load_data()
