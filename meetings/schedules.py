from datetime import time, timedelta, datetime
from collections import defaultdict
from .models import Meeting, Employee

OFFICE_SCHEDULE_START = time(8, 0)
OFFICE_SCHEDULE_END = time(17, 0)
LUNCH_SCHEDULE_START = time(12, 0)
LUNCH_SCHEDULE_END = time(13, 0)

def get_available_schedules():
    all_times = set()
    current_time = OFFICE_SCHEDULE_START
    while current_time < OFFICE_SCHEDULE_END:
        if current_time < LUNCH_SCHEDULE_START or current_time >= LUNCH_SCHEDULE_END:
            all_times.add(current_time)
        current_time = (datetime.combine(datetime.today(), current_time) + timedelta(minutes=30)).time()

    meetings = Meeting.objects.all()

    for meeting in meetings:
        meeting_start = meeting.start_time
        meeting_end = meeting.end_time
        current_time = meeting_start

        while current_time < meeting_end:
            if current_time in all_times:
                all_times.remove(current_time)
            current_time = (datetime.combine(datetime.today(), current_time) + timedelta(minutes=30)).time()

    time_attendees = defaultdict(set)
    for time_point in all_times:
        attendees = set()
        for person in Employee.objects.all():
            meetings = Meeting.objects.filter(person=person, start_time__lte=time_point, end_time__gt=time_point)
            if meetings.exists():
                attendees.add(person.name)
        if len(attendees) >= 3:
            time_attendees[time_point] = list(attendees)

    return time_attendees
