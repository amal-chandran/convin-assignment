from __future__ import absolute_import, unicode_literals
from celery import shared_task
from time import sleep
from .models import Task, TaskTracker
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task
def weekly_task():
    tasks_scheduled = TaskTracker.objects.filter(
        update_type=TaskTracker.WEEKLY)
    tasks_scheduled = map(lambda taskTracker: (Task.objects.filter(
        task_type=taskTracker.task_type), taskTracker), tasks_scheduled)

    for (tasks, tracker) in tasks_scheduled:
        logger.info(f"Mail to {tracker.email} {tasks}")


@shared_task
def daily_task():
    tasks_scheduled = TaskTracker.objects.filter(
        update_type=TaskTracker.DAILY)
    tasks_scheduled = map(lambda taskTracker: (Task.objects.filter(
        task_type=taskTracker.task_type), taskTracker), tasks_scheduled)

    for (tasks,tracker) in tasks_scheduled:
        logger.info(f"Mail to {tracker.email} {tasks}")


@shared_task
def monthly_task():
    tasks_scheduled = TaskTracker.objects.filter(
        update_type=TaskTracker.MONTHLY)
    tasks_scheduled = map(lambda taskTracker: (Task.objects.filter(
        task_type=taskTracker.task_type), taskTracker), tasks_scheduled)

    for (tasks,tracker) in tasks_scheduled:
        logger.info(f"Mail to {tracker.email} {tasks}")
