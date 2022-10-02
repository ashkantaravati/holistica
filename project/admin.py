from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "title",
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
