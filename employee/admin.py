from atexit import register
import imp
from django.contrib import admin
from .models import Employee, LeaveRequest

# Register your models here.
admin.site.register(Employee)
admin.site.register(LeaveRequest)
