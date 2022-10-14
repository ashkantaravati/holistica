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
