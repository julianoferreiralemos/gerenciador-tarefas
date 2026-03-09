from django.db import models
from django.contrib.auth.models import User
from apps.core.models import BaseModel
from .managers import TaskManager


class Task(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = TaskManager()

    def __str__(self):
        return self.title