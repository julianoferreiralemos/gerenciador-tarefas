from django.db import models


class TaskManager(models.Manager):

    def active(self):
        return self.filter(is_active=True)

    def completed(self):
        return self.filter(completed=True)

    def pending(self):
        return self.filter(completed=False)