from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Course(models.Model):
    name = models.CharField(max_length=60)
    students = models.ManyToManyField('Student')

    def __str__(self):
        return self.name
