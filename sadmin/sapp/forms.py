from django.forms import ModelForm
from .models import Course, Student


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'last_nane': 'Last Name'
        }


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        labels = {
            'name': 'Course Name'
        }
