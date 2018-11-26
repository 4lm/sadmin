from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Student
from .forms import StudentForm, CourseForm


def course_details(request, pk=None):
    if pk is None:
        course = Course()
        page_title = 'Add new Course'
    else:
        course = get_object_or_404(Course, pk=pk)
        page_title = 'Edit Course'

    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course saved successfully.')
            return redirect('index')
        else:
            messages.error(request, 'Input incorrect.')
            pass
    else:
        form = CourseForm(instance=course)

    return render(request, 'sapp/course_details.html', {'page_title': page_title, 'form': form})


def student_details(request, pk=None):
    if pk is None:
        student = Student()
        page_title = 'Add new Student'
    else:
        student = get_object_or_404(Student, pk=pk)
        page_title = 'Edit Student'

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student saved successfully.')
            return redirect('index')
        else:
            messages.error(request, 'Input incorrect.')
            pass
    else:
        form = StudentForm(instance=student)

    return render(request, 'sapp/student_details.html', {'page_title': page_title, 'form': form})


def index(request):
    courses = Course.objects.all().order_by('name')
    students = Student.objects.all().order_by('last_name')

    return render(request, 'sapp/index.html', {'page_title': 'SADMIN: Student Administration', 'courses': courses, 'students': students})
