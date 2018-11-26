from django.forms import ModelForm
from .models import Student


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'last_nane': 'Last Name'
        }
