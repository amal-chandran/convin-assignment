from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Task, TaskTracker


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['task_type', 'task_desc']


class TaskTrackerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TaskTracker
        fields = ['task_type', 'update_type', 'email']
