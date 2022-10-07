import datetime
from django.db import models
from django.db.models import Sum
from django.core.validators import MaxValueValidator, MinValueValidator


class Project(models.Model):
    title = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    projected_start_date = models.DateField()
    projected_finish_date = models.DateField()
    actual_start_date = models.DateField(null=True, blank=True)
    actual_finish_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

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

    @property
    def total_weights(self):
        return self.deliverables.aggregate(Sum("weight"))["weight__sum"]

    @property
    def total_progress(self):
        items = self.deliverables.all()
        return sum([item.value for item in items]) / self.total_weights


class Deliverable(models.Model):
    title = models.CharField(max_length=150)
    descriptions = models.TextField(null=True, blank=True)
    progress = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(0)], default=0, blank=True
    )
    weight = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1)], default=1, blank=True
    )
    project = models.ForeignKey(
        to=Project, related_name="deliverables", on_delete=models.CASCADE
    )

    @property
    def value(self):
        return self.progress * self.weight
