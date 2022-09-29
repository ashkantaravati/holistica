import datetime

from employee.utils import EventMapper
from .models import Employee
from django.shortcuts import render


def home(request):
    today = datetime.date.today()
    birthdays_today = Employee.objects.filter(date_of_birth=today)
    events = EventMapper.map_all_employee_birthdays_to_event(birthdays_today)
    auth = {"username": request.user.get_username()}
    return render(request, "employee/index.html", {"auth": auth, "events": events})
