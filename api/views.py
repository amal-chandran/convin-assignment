from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer, TaskSerializer, TaskTrackerSerializer
from .models import Task, TaskTracker


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskTrackerViewSet(viewsets.ModelViewSet):
    queryset = TaskTracker.objects.all()
    serializer_class = TaskTrackerSerializer
