from django.db import models

GENDER_CHOICES = (("F", "Female"), ("M", "Male"))


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name
#TODo : implement employee_status (hired,not_hired,staff,tech,...) + 

class LeaveRequest(models.Model):
    class DurationType(models.IntegerChoices):
        Hours = 1
        Days = 2

    starting_from = models.DateTimeField()
    duration_type = models.IntegerField(choices=DurationType.choices)
    duration = models.SmallIntegerField()

    employee = models.ForeignKey(
        to=Employee, on_delete=models.CASCADE, related_name="leave_requests"
    )
    substitute = models.ForeignKey(
        to=Employee,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="substitute_accountabilities",
    )
    reason = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Employee_Performance (models.Model):
    # Time, attendance, and leave 
    employee = models.ForeignKey(
        to=Employee, on_delete=models.CASCADE, related_name="leave_requests"
    )
    arrive_time = models.DateTimeField()
    leave_time = models.DateTimeField()
    attendance = models.DateTimeField()
    def attendance(leave_time,arrive_time):
        attendance = leave_time - arrive_time
        return attendance

class Employee_Finance (models.Model): 
    pass

class task ():
    employee = models.ForeignKey(
        to=Employee, on_delete=models.CASCADE, related_name="leave_requests"
    )
    # task_status,task_duration,task_start_date,task_end_date,

class Team () : 
    # Team_name, Team_Skill, Team_scope, team_members, team_objectives, team_tasks, 
    pass
