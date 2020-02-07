from django.db import models
from .validators import validate_task_type


class Task(models.Model):
    task_type = models.IntegerField(validators=[validate_task_type])
    task_desc = models.CharField(max_length=200)

    def __str__(self):
        return self.task_desc

class TaskTracker(models.Model):
    WEEKLY = 'W'
    DAILY = 'D'
    MONTHLY = 'M'

    UPDATE_CHOICES = [
        (WEEKLY, 'WEEKLY'),
        (DAILY, 'DAILY'),
        (MONTHLY, 'MONTHLY'),
    ]

    task_type = models.IntegerField(validators=[validate_task_type])

    update_type = models.CharField(
        choices=UPDATE_CHOICES, default=WEEKLY, max_length=1)

    email = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.email} {self.task_type}"
