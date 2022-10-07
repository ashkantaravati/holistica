from django.contrib import admin
from .models import Deliverable, Project


class DeliverableInline(admin.TabularInline):
    model = Deliverable


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [DeliverableInline]

    list_display = (
        "title",
        "total_progress",
        "age",
        "delay",
        "projected_duration",
        "actual_start_date",
        "actual_finish_date",
        "projected_start_date",
        "projected_finish_date",
        "updated_at",
        "created_at",
    )
