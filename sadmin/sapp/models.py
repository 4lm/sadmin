from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Course(models.Model):
    name = models.CharField(max_length=60)
    students = models.ManyToManyField('Student', on_delete=models.CASCADE)
