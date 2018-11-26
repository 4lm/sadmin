from django.shortcuts import render
from .models import Course, Student


def list_courses(request):
    courses = Course.objects.all().order_by('name')

    return render(request, 'sapp/list_courses.html', {'page_title': 'Course List', 'courses': courses})
