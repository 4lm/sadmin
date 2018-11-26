from django.forms import ModelForm
from .models import Course, Student


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        labels = {
            'name': 'Course name'
        }
