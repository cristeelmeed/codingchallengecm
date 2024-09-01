from datetime import time, timedelta, datetime
from collections import defaultdict
from .models import Meeting, Employee

MEETING_TIME = timedelta(minutes=30)
OFFICE_SCHEDULE_START = time(8, 0)
OFFICE_SCHEDULE_END = time(17, 0)
LUNCH_SCHEDULE_START = time(12, 0)
LUNCH_SCHEDULE_END = time(13, 0)

def find_available_schedules():
    all_times = set()
    current_time = OFFICE_SCHEDULE_START
    while current_time < OFFICE_SCHEDULE_END:
        if current_time < LUNCH_SCHEDULE_START or current_time >= LUNCH_SCHEDULE_END:
            all_times.add(current_time)
            #print(current_time) #schedules for meeting
        current_time = (datetime.combine(datetime.today(), current_time) + MEETING_TIME).time()


    available_times = defaultdict(list)
    for time_point in sorted(all_times):
        attendees = set()
        #print(time_point) #current schedule
        for employee in Employee.objects.all():
            meetings = Meeting.objects.filter(employee=employee, start_time__lte=time_point, end_time__gt=time_point)
            if not meetings.exists():
                attendees.add(employee.name)
                #print(employee.name + ' employee available')
            #else:
                #print(employee.name + ' employee not available')
        if len(attendees) >= 3:
            available_times[time_point] = list(attendees)

    return available_times