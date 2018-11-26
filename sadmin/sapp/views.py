from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Course, Student
from .forms import StudentForm


def add_student(request):
    student = Student()

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student saved successfully.')
            return HttpResponseRedirect(reverse('list_courses'))
        else:
            messages.error(request, 'Input incorrect.')
            pass
    else:
        form = StudentForm(instance=student)

    return render(request, 'sapp/add_student.html', {'page_title': 'Add Student', 'form': form})


def list_courses(request):
    courses = Course.objects.all().order_by('name')

    return render(request, 'sapp/list_courses.html', {'page_title': 'Course List', 'courses': courses})
