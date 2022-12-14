# Generated by Django 4.1.1 on 2022-10-01 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=150)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("projected_start_date", models.DateField()),
                ("projected_finish_date", models.DateField()),
                ("actual_start_date", models.DateField(blank=True, null=True)),
                ("actual_finish_date", models.DateField(blank=True, null=True)),
            ],
        ),
    ]
