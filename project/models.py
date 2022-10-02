import datetime
from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    projected_start_date = models.DateField()
    projected_finish_date = models.DateField()
    actual_start_date = models.DateField(null=True, blank=True)
    actual_finish_date = models.DateField(null=True, blank=True)

    @property
    def age(self):
        return datetime.date.today() - self.actual_start_date

    @property
    def projected_duration(self):
        return self.projected_finish_date - self.projected_start_date

    @property
    def delay(self):
        target_date = self.actual_finish_date or datetime.date.today()
        return target_date - self.projected_finish_date
