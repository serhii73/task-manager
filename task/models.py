from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class LabelTask(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Task(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.PROTECT, related_name='+')
    name_task = models.CharField(max_length=1000)
    description_task = models.TextField(max_length=10000)
    category_task = models.ForeignKey(Category)
    label_task = models.ManyToManyField(LabelTask, default='', blank=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    deadline_task = models.DateTimeField(blank=True, null=True)
    executive_man = models.ManyToManyField(User)

    def __str__(self):
        return self.name_task
